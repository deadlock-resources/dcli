import os
import sys
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

    if quiet == True:
        cmd += ' &>/dev/null'

    exitCode = os.system(cmd)
    if exitOnError == True and exitCode != 0:
        if spin != None:
            spin.stop()
            jump()
        if exitCode == 2:
            error('Cancelled.')
        else:
            error(messageOnError)
        sys.exit(1)


