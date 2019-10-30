import os
import sys
from PyInquirer import prompt
from ..logger import error
from ..const import TARGET_FILE_FIELD, TARGET_METHOD_FIELD, TARGET_METHOD_ARGS_FIELD, TARGET_METHOD_RETURN_FIELD

def askCppQuestions():
    cppQuestions = [
        {
            'type': 'input',
            'name': TARGET_METHOD_FIELD,
            'message': 'Method for the user, entry point of the program (e.g. methodName):',
        },
        {
            'type': 'input',
            'name': TARGET_METHOD_ARGS_FIELD,
            'message': 'Input: args list for the previous method, what the user will receive (e.g. int amount, double quantity):',
        },
        {
            'type': 'input',
            'name': TARGET_METHOD_RETURN_FIELD,
            'message': 'Output type: return type of the previous method, what the user will have to return (e.g. int):',
        }
    ]
    answers = prompt(cppQuestions)
    if len(answers) == 0:
        error('Cancelled.')
        sys.exit()
    return answers
