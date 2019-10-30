import os
import sys
from .spinCursor import SpinCursor
from .logger import info, error

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
    build(path) 
    info('Running mission..')
    os.system('docker run c Test')
    return ''


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
