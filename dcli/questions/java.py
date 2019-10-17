
import os
import sys
from PyInquirer import prompt
from ..logger import error
from ..const import TARGET_FILE_FIELD, TARGET_METHOD_FIELD

def askJavaQuestions():
    javaQuestions = [
        {
            'type': 'input',
            'name': TARGET_FILE_FIELD,
            'message': 'Main file for the user (e.g. Main):',
        },
        {
            'type': 'input',
            'name': TARGET_METHOD_FIELD,
            'message': 'Main method for the user (e.g. String method(int a)):',
        },
    ]
    answers = prompt(javaQuestions)
    if len(answers) == 0:
        error('Cancelled.')
        sys.exit()
    return answers
