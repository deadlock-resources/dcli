import os
import sys
from ..language import Language
from PyInquirer import prompt
from ...logger import error
from ...const import TARGET_FILE_FIELD, TARGET_METHOD_FIELD, TARGET_METHOD_ARGS_FIELD, TARGET_METHOD_RETURN_FIELD

TEMPLATE_PATH = '/src/main/kotlin/template'
SUCCESS_PATH = '/src/main/kotlin/success'
APP_PATH = '/src/main/kotlin/app'

SOLVE_PATH = '/src/main/kotlin/app/Solve.kt'
RUN_PATH = '/src/main/kotlin/app/Run.kt'

ASSET_PATHS = ['/src/main/kotlin/app/Logger.kt', '/src/main/kotlin/app/Main.kt']

TARGET_FILE = 'Target'

class Kotlin(Language):
    def __init__(self):
        Language.__init__(self,
            'kotlin',
            TEMPLATE_PATH,
            SUCCESS_PATH,
            APP_PATH,
            SOLVE_PATH,
            RUN_PATH,
            TARGET_FILE,
            'kt',
            ASSET_PATHS
        )

    def add_type(self, name):
        self.add_new_asset(self.templateDirPath, name, f'package template\n\nclass {name} {{}}')
        self.add_new_asset(self.successDirPath, name, f'package success\n\nclass {name} {{}}')

    def parse_target_method_args(self, args, arg_type):
        if (arg_type == TARGET_METHOD_RETURN_FIELD):
            return super().parse_target_method_args(args, arg_type)
        else:
            return list(map(lambda s: s.strip().split(":")[1].strip() if s else "", args.split(',')))
        
        
    def ask_questions(self):
        kotlinQuestions = [
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
                'message': 'Input: args list for the previous method, what the user will receive (e.g. amount: Int, quantity: Double), may be empty:',
            },
            {
                'type': 'input',
                'name': TARGET_METHOD_RETURN_FIELD,
                'message': 'Output type: return type of the previous method, what the user will have to return (e.g. String), may be empty:',
            }
        ]
        answers = prompt(kotlinQuestions)
        if len(answers) == 0:
            error('Cancelled.')
            sys.exit()
        return answers
