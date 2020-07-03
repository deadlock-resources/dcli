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

from distutils.dir_util import copy_tree

def build(tag, path):
    spin = SpinCursor('', speed=5, maxspin=100000)
    if (os.path.exists(path) == False):
        error('Directory does not exist ' + path)
        sys.exit(1)
    info('🔨 Building mission..')
    spin.start()
    exitCode = 0
    if (os.path.exists(f'{path}/build.sh')):
        exitCode = os.system(f'{path}/build.sh')
        exitIfError(exitCode, 'Cannot exec build.sh file', spin)
    info('🐳 Building Docker image')
    exitCode += os.system(f'docker build {path} -q -t {tag}')
    exitIfError(exitCode, 'Cannot build Docker image..', spin)
    spin.stop()

def exitIfError(exitCode, message, spin):
    if (exitCode != 0):
        spin.stop()
        jump()
        if (exitCode == 2):
            error('Cancelled.')
        else:
            error(message)
        sys.exit(1)

def run(path='.', language='empty'):
    '''
    Run the mission under given path.
    As if user clicked on Run button.

    :param path: path of your mission. Default: .
    '''
    yaml = loadYaml(path + '/' + CHALLENGE_YAML)
    if 'coding' in yaml:
        if os.path.exists('entry.rs') == True:
            runMetamorphCode(path, language)
        else:
            runCode(path)
    elif 'hacking' in yaml:
        runHack(path)
    else:
        error('Challenge type not supported, verify your challenge.yaml')

def prepareMetamorphCode(path, tmpDir):
    info('🔨 Building mission..')
    spin = SpinCursor('', speed=5, maxspin=100000)
    spin.start()

    try:
        copy_tree(path, tmpDir.name)
        shutil.copy(getPathFromRoot('utils/Dockerfile-runner'), tmpDir.name + '/Dockerfile')
        shutil.copy(getPathFromRoot('utils/run.sh'), tmpDir.name + '/run.sh')

        # copy each template files
        for subdir, dirs, files in os.walk(path + '/template'):
            for file in files:
                shutil.copy(os.path.join(subdir, file), tmpDir.name)


        os.system('docker build ' + tmpDir.name + ' -q -t meta')
    finally:
        spin.stop()

def runMetamorphCode(path, language):
    downloadIfNecessary(path)

    # copy everything to tmp to avoid any conflict with user directory files
    tmpDir = tempfile.TemporaryDirectory()
    prepareMetamorphCode(path, tmpDir)

    # volume to the tmp dir
    os.system(f"docker run -v {tmpDir.name}:/tmp/runner meta run {language}")

def solveMetamorphCode(path, language):
    downloadIfNecessary(path)

    # copy everything to tmp to avoid any conflict with user directory files
    tmpDir = tempfile.TemporaryDirectory()
    prepareMetamorphCode(path, tmpDir)

    # volume to the tmp dir
    os.system(f"docker run -v {tmpDir.name}:/tmp/runner meta solve {language}")


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


def runCode(path='.'):
    tag = uuid.uuid4()
    build(tag, path) 
    info('🚀 Running mission..')
    os.system(f'docker run {tag} Run')
    pass

def runHack(path='.'):
    os.system(getPathFromRoot('utils/run-hack.sh'))


def solveScore(tag, path='.'):
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


def solveCode(tag, path='.', ):
    info('🚀 Solving mission..')
    os.system(f'docker run {tag} Solve')
    pass

def solve(path='.', language='empty'):
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

