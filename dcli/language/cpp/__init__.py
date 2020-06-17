import os
import sys
from ..language import Language
from PyInquirer import prompt
from ...logger import error
from ...const import TARGET_FILE_FIELD, TARGET_METHOD_FIELD, TARGET_METHOD_ARGS_FIELD, TARGET_METHOD_RETURN_FIELD

TEMPLATE_PATH = '/src/template'
SUCCESS_PATH = '/src/success'
APP_PATH = '/src/app'

SOLVE_PATH = '/src/app/main.cpp'
RUN_PATH = '/src/app/main.cpp'

ASSET_PATHS = ['src/Makefile', 'src/template/Target.h', 'src/app/Logger.cpp', 'src/app/Logger.h']

TARGET_FILE = 'Target'

class Cpp(Language):
    def __init__(self):
        Language.__init__(self,
            'cpp',
            TEMPLATE_PATH,
            SUCCESS_PATH,
            APP_PATH,
            SOLVE_PATH,
            RUN_PATH,
            TARGET_FILE,
            'cpp',
            ASSET_PATHS
        )

    def ask_questions(self):
        cppQuestions = [
            {
                'type': 'input',
                'name': TARGET_METHOD_FIELD,
                'message': 'Method for the user, entry point of the program (e.g. methodName):',
                'validate': lambda text: (len(text) > 0 and text != 'main' or 'main is a reserved method.') or 'Must not be empty.'
            },
            {
                'type': 'input',
                'name': TARGET_METHOD_ARGS_FIELD,
                'message': 'Input: args list for the previous method, what the user will receive (e.g. int amount, double quantity):',
            },
            {
                'type': 'input',
                'name': TARGET_METHOD_RETURN_FIELD,
                'message': 'Output type: return type of the previous method, what the user will have to return (e.g. int), may be empty:',
            }
        ]
        answers = prompt(cppQuestions)
        if len(answers) == 0:
            error('Cancelled.')
            sys.exit()
        return answers

    def get_default_uncommon_type_value(self, current_type):
        return f'{current_type}()'

    def add_type(self, name):
        template = ("#include <ostream>\n"
                    "include \"" + name + ".h\"\n"
                    "// " + name + " class implementation\n"
                    "std::ostream &operator<<(std::ostream &os, " + name + " const &m) {\n"
                    "    return os << \"" + name + "\";\n"
                    "}\n")
        self.add_new_asset(self.templateDirPath, name, f'class {name} {{}};', 'h')
        self.add_new_asset(self.templateDirPath, name, template, self.extension)

    def get_assets_to_import(self):
        assets_to_import = []
        for asset in self.newAssets:
            if asset.extension == 'h':
                assets_to_import.append(asset)
        return assets_to_import