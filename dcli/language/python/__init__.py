import os
import sys
from ..language import Language
from PyInquirer import prompt
from ...logger import error
from ...const import TARGET_FILE_FIELD, TARGET_METHOD_FIELD


TEMPLATE_PATH = '/src/main/python/template'
SUCCESS_PATH = '/src/main/python/success'
APP_PATH = '/src/main/python/app'

SOLVE_PATH = '/src/main/python/Solve.py'
RUN_PATH = '/src/main/python/Run.py'

TARGET_FILE = '__init__'

class Python(Language):
    def __init__(self):
        Language.__init__(self,
            'python',
            TEMPLATE_PATH,
            SUCCESS_PATH,
            APP_PATH,
            SOLVE_PATH,
            RUN_PATH,
            TARGET_FILE,
            'py'
        )

    def ask_questions(self):
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

    def need_to_generate_new_type(self):
        return False