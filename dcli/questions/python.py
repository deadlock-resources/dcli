
import os
import sys
from PyInquirer import prompt
from ..logger import error
from ..const import TARGET_FILE_FIELD, TARGET_METHOD_FIELD

def askPythonQuestions():
    pythonQuestions = [
        {
            'type': 'input',
            'name': TARGET_METHOD_FIELD,
            'message': 'Main method for the user (e.g. method_name(a)):',
        },
    ]
    answers = prompt(pythonQuestions)
    if len(answers) == 0:
        error('Cancelled.')
        sys.exit()
    return answers
