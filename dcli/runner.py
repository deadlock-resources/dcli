import os
import sys
import json
import uuid
from multiprocessing import Process
from .model.missionUserScore import MissionUserScore
from .generator.file import getPathFromRoot, loadYaml, createTmpFolder, writeFile
from .spinCursor import SpinCursor
from .logger import info, error
from .const import CHALLENGE_YAML, API_PORT, MISSION_USER_SCORE_ENDPOINT, MISSION_USER_SCORE_FILENAME, API_ADRESS
from .scoreController import startScoreResource

def build(path):
    spin = SpinCursor('', speed=5, maxspin=50)
    if (os.path.exists(path) == False):
        error('Directory does not exist ' + path)
        sys.exit()
    info('Building mission..')
    spin.start()
    os.system('docker build ' + path + ' -q -t c')
    spin.stop()

def run(path='.'):
    '''
    Run the mission under given path.
    As if user clicked on Run button.

    :param path: path of your mission. Default is .
    '''
    yaml = loadYaml(path + '/' + CHALLENGE_YAML)
    if 'coding' in yaml:
        runCode(path)
    elif 'hacking' in yaml:
        runHack(path)
    else:
        error('Challenge type not supported, verify your challenge.yaml')

def runCode(path='.'):
    build(path) 
    info('Running mission..')
    os.system('docker run c Run')
    pass

def runHack(path='.'):
    runHackScriptPath = getPathFromRoot('utils/run-hack.sh')
    os.system(runHackScriptPath)


def solveScore(path='.'):
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
    os.system(f'docker run --network="host" -v {tmpPathFile}:/tmp/{MISSION_USER_SCORE_FILENAME} c Solve')
    httpServerProcess.terminate()


def solveCode(path='.'):
    info('Solving mission..')
    os.system('docker run c Solve')
    pass

def solve(path='.'):
    '''
    Run Solve step for the mission under given path.
    As if user clicked on Submit button.

    :param path: path of your mission. Default is .
    '''
    build(path)
    yaml = loadYaml(path + '/' + CHALLENGE_YAML)
    if 'coding' in yaml:
        if 'score' in yaml['coding']:
            solveScore(path)
        else:
            solveCode(path)
    else:
        error('Challenge type not supported for solve method.')

