import os
import sys
import json
import uuid
from multiprocessing import Process
from .model.missionUserScore import MissionUserScore
from .generator.file import getPathFromRoot, loadYaml, createTmpFolder, writeFile
from .spinCursor import SpinCursor
from .logger import info, error, jump
from .const import CHALLENGE_YAML, API_PORT, MISSION_USER_SCORE_ENDPOINT, MISSION_USER_SCORE_FILENAME, API_ADRESS
from .scoreController import startScoreResource

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
        exitIfError(exitCode, 'Cannot exec build.sh file')
    info('🐳 Building Docker image')
    exitCode += os.system(f'docker build {path} -q -t {tag}');
    exitIfError(exitCode, 'Cannot build Docker image..')
    spin.stop()

def exitIfError(exitCode, message):
    if (exitCode != 0):
        spin.stop()
        jump()
        if (exitCode == 2):
            error('cancel')
        else:
            error(message)
        sys.exit(1)

def run(path='.'):
    '''
    Run the mission under given path.
    As if user clicked on Run button.

    :param path: path of your mission. Default: .
    '''
    yaml = loadYaml(path + '/' + CHALLENGE_YAML)
    if 'coding' in yaml:
        runCode(path)
    elif 'hacking' in yaml:
        runHack(path)
    else:
        error('Challenge type not supported, verify your challenge.yaml')

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

def solve(path='.'):
    '''
    Run Solve step for the mission under given path.
    As if user clicked on Submit button.

    :param path: path of your mission. Default: .
    '''
    tag = uuid.uuid4()
    build(tag, path)
    yaml = loadYaml(path + '/' + CHALLENGE_YAML)
    if 'coding' in yaml:
        if 'score' in yaml['coding']:
            solveScore(tag, path)
        else:
            solveCode(tag, path)
    else:
        error('Challenge type not supported for solve method.')

