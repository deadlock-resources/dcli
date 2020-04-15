import time
import os
import sys
import json
import uuid
import requests
import hashlib
import shutil
import tempfile
from multiprocessing import Process
from .model.missionUserScore import MissionUserScore
from .generator.file import getPathFromRoot, loadYaml, createTmpFolder, writeFile
from .spinCursor import SpinCursor
from .logger import info, error, jump
from .const import CHALLENGE_YAML, API_PORT, MISSION_USER_SCORE_ENDPOINT, MISSION_USER_SCORE_FILENAME, API_ADRESS
from .scoreController import startScoreResource
from .cmd import execute

from distutils.dir_util import copy_tree

DOCKER_NETWORK = 'deadlock-challenge'
PREFIX_SERVICE_NAME='deadlock-service'

def build(tag, path):
    spin = SpinCursor('', speed=5, maxspin=100000)
    if (os.path.exists(path) == False):
        error('Directory does not exist ' + path)
        sys.exit(1)
    info('🔨 Building mission..')
    spin.start()

    if (os.path.exists(f'{path}/build.sh')):
        execute(f'{path}/build.sh', {
            'exitOnError': True,
            'messageOnError': 'Cannot execute build.sh file',
            'spin': spin})
    info('🐳 Building Docker image')
    execute(f'docker build {path} -q -t {tag}', {
            'quiet': True,
            'exitOnError': True,
            'spin': spin})

    execute(f'docker network create {DOCKER_NETWORK}', {'quiet': True})

    # also build services if exist
    if os.path.exists(f'{path}/services') == True:
        dirs = os.listdir(f'{path}/services')
        for service in dirs:
            buildAndRunService(f'{path}/services', service)
            
    spin.stop()

def buildAndRunService(path, service):
    info(f'📂 {service} service found')
    info(f'>  🐳 Building {service}')
    execute(f'docker build -q -f {path}/{service}/Dockerfile -t {getDockerServiceName(service)} {path}/{service}', {"quiet": False})
    info(f'>  🚀 Running {service}')
    execute(f'docker run -d --rm --net={DOCKER_NETWORK} --name {service} {getDockerServiceName(service)}', {"quiet": False})


def getDockerServiceName(serviceName):
    return f'{PREFIX_SERVICE_NAME}-{serviceName}'

def clean():
    print('')
    time.sleep(1)
    info('Cleaning resources')
    execute(f'docker ps --filter network={DOCKER_NETWORK} -aq | xargs -r docker stop >/dev/null | xargs -r docker rm', {"quiet": True})
    execute(f'docker network rm {DOCKER_NETWORK}', {"quiet": True})
    info('Done')

def exitIfError(exitCode, message, spin):
    if (exitCode != 0):
        spin.stop()
        jump()
        if (exitCode == 2):
            error('Cancelled.')
        else:
            error(message)
        sys.exit(1)

def run(path=os.getcwd(), language='empty'):
    '''
    Run the mission under given path.
    As if user clicked on Run button.

    :param path: path of your mission. Default: .
    '''
    yaml = loadYaml(path + '/' + CHALLENGE_YAML)
    if 'coding' in yaml:
        if os.path.exists(f'{path}/entry.rs') == True:
            runMetamorphCode(path, language)
        else:
            runCode(path)
    elif 'hacking' in yaml:
        runHack(path)
    else:
        error('Challenge type not supported, verify your challenge.yaml')
    clean()

def prepareMetamorphCode(path, tmpDir):
    info('🔨 Building mission..')
    spin = SpinCursor('', speed=5, maxspin=100000)
    spin.start()

    try:
        copy_tree(path, tmpDir)
        shutil.copy(getPathFromRoot('utils/Dockerfile-runner'), tmpDir + '/Dockerfile')
        shutil.copy(getPathFromRoot('utils/run.sh'), tmpDir + '/run.sh')

        # copy each template files
        for subdir, dirs, files in os.walk(path + '/template'):
            for file in files:
                shutil.copy(os.path.join(subdir, file), tmpDir)


        os.system('docker build ' + tmpDir + ' -q -t meta')
    finally:
        spin.stop()

def runMetamorphCode(path, language):
   execMetamorphCode(path, language, 'run') 

def solveMetamorphCode(path, language):
   execMetamorphCode(path, language, 'solve') 
    

def execMetamorphCode(path, language, way):
    if path == '.':
        path = os.getcwd()
    elif path[0] != '/':
        error('Path given must be absolute')
        exit(1)
        
    downloadIfNecessary(path)

    # copy everything to tmp to avoid any conflict with user directory files
    # cannot use the default /tmp dir, because it generate problem with Docker volume
    tmpDir = f'{path}/build'
    prepareMetamorphCode(path, tmpDir)

    # volume to the tmp dir
    os.system(f"docker run -v {tmpDir}:/tmp/runner meta {way} {language}")
    shutil.rmtree(tmpDir, ignore_errors=True)


def downloadIfNecessary(path):
    should_download = True
    if os.path.exists(path + '/runner'):
        if os.path.exists(path + '/.hash'):
            entry_hash = open(path + '/.hash', 'r').read()
            if entry_hash == hashlib.md5(open('entry.rs', 'rb').read()).hexdigest():
                should_download = False

    if should_download == True:
        downloadRunner(path)
    
def downloadRunner(path):
    url = "https://builder.staging.deadlock.io/build"
    
    info('🛰️  Download runner based on your entry.rs file.')
    info('Operation will be long the first time, no worries.')

    spin = SpinCursor('', speed=5, maxspin=100000)
    spin.start()
    runner_bin = 'runner'
    files = {'file': open('entry.rs', 'rb')}
    response = requests.post(url, files=files, stream=True)
    spin.stop()

    if response.status_code != 200:
        print(response.text)
        print(response.content)
        error('Cannot build your entry.rs, check its correct.')
        exit(1)

    with open(runner_bin, 'wb') as f:
        shutil.copyfileobj(response.raw, f)

    os.system('chmod u+x runner')

    # write runner hash
    with open(path + '/.hash', 'w+') as f:
        with open('entry.rs', 'rb') as entry:
            h = hashlib.md5(entry.read()).hexdigest()
            f.write(h)

    info('🛰️  Download completed')


def runCode(path=os.getcwd()):
    tag = uuid.uuid4()
    build(tag, path) 
    info('🚀 Running mission..')
    execute(f'docker run --net={DOCKER_NETWORK} {tag} Run')
    pass

def runHack(path=os.getcwd()):
    os.system(getPathFromRoot('utils/run-hack.sh'))


def solveScore(tag, path=os.getcwd()):
    '''
    Run Solve step for the mission under given path.
    As if user clicked on Submit button.
    Create and mount all necessaries files to be able to post the score somewhere.

    :param path: path of your mission. Default is .
    '''
    info('Setting up environment..')

    info('Starting http server..')
    httpServerProcess = Process(target=startScoreResource)
    httpServerProcess.start()

    info('Writing file..')
    tmpPathFile = createTmpFolder() + '/' + MISSION_USER_SCORE_FILENAME
    missionUserScore = MissionUserScore(str(uuid.uuid4()), f'http://{API_ADRESS}:{str(API_PORT)}{MISSION_USER_SCORE_ENDPOINT}').__dict__
    missionUserScoreJson = json.dumps(missionUserScore)
    writeFile(tmpPathFile, missionUserScoreJson)

    info('Starting mission score..')
    os.system(f'docker run --network="host" -v {tmpPathFile}:/tmp/{MISSION_USER_SCORE_FILENAME} {tag} Solve')
    httpServerProcess.terminate()


def solveCode(tag, path=os.getcwd()):
    info('🚀 Solving mission..')
    os.system(f'docker run --net={DOCKER_NETWORK} {tag} Solve')
    pass

def solve(path=os.getcwd(), language='empty'):
    '''
    Run Solve step for the mission under given path.
    As if user clicked on Submit button.

    :param path: path of your mission. Default: .
    '''
    yaml = loadYaml(path + '/' + CHALLENGE_YAML)
    if 'coding' in yaml:
        if os.path.exists(path + '/entry.rs') == True:
            solveMetamorphCode(path, language)
        elif 'score' in yaml['coding']:
            tag = uuid.uuid4()
            build(tag, path)
            solveScore(tag, path)
        else:
            tag = uuid.uuid4()
            build(tag, path)
            solveCode(tag, path)
    else:
        error('Challenge type not supported for solve method.')
    clean()

