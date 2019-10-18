from .logger import info
import os

def run(path='.'):
    '''
    Run the mission under given path.
    As if user clicked on Run button.

    :param path: path of your mission. Default is .
    '''
    info('Building mission..')
    os.system('docker build ' + path + ' -q -t c')
    info('Running mission..')
    os.system('docker run c run')
    return ''


def solve(path='.'):
    '''
    Run Solve step for the mission under given path.
    As if user clicked on Submit button.

    :param path: path of your mission. Default is .
    '''
    info('Building mission..')
    os.system('docker build ' + path + ' -q -t c')
    info('Running mission..')
    os.system('docker run c Solve')
    return ''
