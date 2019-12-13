import os
import sys
from .generator.file import getPathFromRoot, loadYaml
from .spinCursor import SpinCursor
from .logger import info, error
from .const import CHALLENGE_YAML

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
    yaml = loadYaml(path + '/' + CHALLENGE_YAML)
    if 'coding' in yaml:
        runCode(path)
    elif 'hacking' in yaml:
        runHack(path)
    else:
        error('Challenge type not supported, verify your challenge.yaml')

def runCode(path='.'):
    '''
    Run the mission under given path.
    As if user clicked on Run button.

    :param path: path of your mission. Default is .
    '''
    build(path) 
    info('Running mission..')
    os.system('docker run c Run')
    return ''

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
    build(path)
    info('Solving mission score..')

def solve(path='.'):
    '''
    Run Solve step for the mission under given path.
    As if user clicked on Submit button.

    :param path: path of your mission. Default is .
    '''
    build(path)
    info('Solving mission..')
    os.system('docker run c Solve')
    return ''
