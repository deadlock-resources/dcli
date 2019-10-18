from .logger import info
import os

def run(self, path='.'):
    pass


def solve(self, path='.'):
    """Run mission under given path.
    default path: ./
    """
    info('Building mission..')
    os.system('docker build ' + path + ' -q -t c')
    info('Running mission..')
    os.system('docker run c Solve')
    return ''
