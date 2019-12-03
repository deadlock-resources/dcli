
import os
import sys
from PyInquirer import prompt
from ..logger import error
from ..const import TARGET_FILE_FIELD, TARGET_METHOD_FIELD, TARGET_METHOD_ARGS_FIELD, TARGET_METHOD_RETURN_FIELD

def askJavaQuestions():
    javaQuestions = [
        {
            'type': 'input',
            'name': TARGET_FILE_FIELD,
            'message': 'Main file for the user, (e.g. MainFile) without extension:',
        },
        {
            'type': 'input',
            'name': TARGET_METHOD_FIELD,
            'message': 'Main method for the user, entry point of the program (e.g. mainMethod):',
            'validate': lambda text: (len(text) > 0 and text != 'main' or 'main is a reserved method.') or 'Must not be empty.'
        },
        {
            'type': 'input',
            'name': TARGET_METHOD_ARGS_FIELD,
            'message': 'Input: args list for the previous method, what the user will receive (e.g. int amount, double quantity), may be empty:',
        },
        {
            'type': 'input',
            'name': TARGET_METHOD_RETURN_FIELD,
            'message': 'Output type: return type of the previous method, what the user will have to return (e.g. String), may be empty:',
        }
    ]
    answers = prompt(javaQuestions)
    if len(answers) == 0:
        error('Cancelled.')
        sys.exit()
    return answers
