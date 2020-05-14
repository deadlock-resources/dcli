import os
import sys
from ..language import Language
from PyInquirer import prompt
from ...logger import error
from ...const import TARGET_FILE_FIELD, TARGET_METHOD_FIELD, TARGET_METHOD_ARGS_FIELD, TARGET_METHOD_RETURN_FIELD

TEMPLATE_PATH = '/src/main/java/template'
SUCCESS_PATH = '/src/main/java/success'
APP_PATH = '/src/main/java/app'

SOLVE_PATH = '/src/main/java/app/Solve.java'
RUN_PATH = '/src/main/java/app/Run.java'

ASSET_PATHS = ['/src/main/java/app/Logger.java']

TARGET_FILE = 'Target'

class Java(Language):
    def __init__(self):
        Language.__init__(self,
            'java',
            TEMPLATE_PATH,
            SUCCESS_PATH,
            APP_PATH,
            SOLVE_PATH,
            RUN_PATH,
            TARGET_FILE,
            'java',
            ASSET_PATHS
        )
    
    def add_type(self, name):
        self.add_new_asset(self.templateDirPath, name, f'package template;\n\nclass {name} {{}}')
        self.add_new_asset(self.successDirPath, name, f'package success;\n\nclass {name} {{}}')

    def ask_questions(self):
        javaQuestions = [
            {
                'type': 'input',
                'name': TARGET_FILE_FIELD,
                'message': 'Main file for the user, (e.g. MainFile) without extension:',
                'validate': lambda text: len(text) > 0 or 'Must not be empty.'
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