import os
import sys
import subprocess
try:
    from subprocess import DEVNULL
except ImportError:
    import os
    DEVNULL = open(os.devnull, 'wb')
from .logger import info, error, jump


def execute(cmd, args = {}):
    '''
    :param cmd: Command to execute
    :param args: a dico, may contains:
                        exitOnError: True|False, default to False
                        messageOnError: String, default to `Something went wrong`
                        quiet: True|False, default to False
                        spin: Spinner, default to None
    '''
    messageOnError = args.get("messageOnError", "Something went wrong")
    exitOnError = args.get("exitOnError", False)
    quiet = args.get("quiet", False)
    spin = args.get("spin", None)

    FNULL = open(os.devnull, 'w')


    try:
        exitCode = 0
        if quiet == True:
            exitCode = subprocess.call(cmd, shell=True, stdout=DEVNULL, stderr=DEVNULL)
        else:
            exitCode = subprocess.call(cmd, shell=True)
        if spin != None:
            spin.stop()
            spin = None
        if exitOnError == True and exitCode != 0:
            error(messageOnError)
            sys.exit(1)
    except KeyboardInterrupt:
        error('Cancelled.')
        sys.exit(2)
    except OSError as e:
        error('Something bad happened:')
        error(messageOnError)
    if spin != None:
        spin.stop()
        jump()


