import sys

from PyInquirer import prompt

from .const import TARGET_METHOD_FIELD, TARGET_METHOD_RETURN_FIELD, TARGET_METHOD_ARGS_FIELD, TARGET_FILE_FIELD
from .generator.languageGenerator import LanguageGenerator
from .language.c import C
from .language.cpp import Cpp
from .language.java import Java
from .language.python import Python
from .language.types_helper import get_datatype_from_user
from .logger import info, error, paragraph

LANGUAGES = dict({
    'java': Java(),
    'cpp': Cpp(),
    'c': C(),
    'python': Python()
})


def askUsual():
    questions = [
        {
            'type': 'input',
            'name': 'name',
            'message': 'Name (e.g. code_your_challenge_name):',
            'validate': lambda text: len(text) > 0 or 'Must not be empty.'
        },
        {
            'type': 'input',
            'name': 'label',
            'message': 'Title (e.g. Building rockets)',
            'validate': lambda text: len(text) > 0 or 'Must not be empty.'
        },
        {
            'type': 'input',
            'name': 'description',
            'message': 'Description (e.g. Challenge to learn building rockets and save the world!):',
            'validate': lambda text: len(text) > 0 or 'Must not be empty.'
        },
        {
            'type': 'list',
            'name': 'level',
            'message': 'Level (easiest to hardest):',
            'choices': [
                'jarjarbinks', 'ewok', 'padawan', 'jedi', 'master'
            ],
        },
        {
            'type': 'list',
            'name': 'language',
            'message': 'Choose your language',
            'choices':
                LANGUAGES.keys()
            ,
        }

    ]
    answers = prompt(questions)
    if len(answers) == 0:
        error('Cancelled.')
        sys.exit()
    return answers


def \
        commonEndingMessage(answers):
    info('You have to complete many //TODO within the generated mission.')
    info('Then you will be able to test your mission with:')
    paragraph('dcli run ./' + answers['name'])
    paragraph('dcli solve ./' + answers['name'])


class Generator():

    def generate(self):
        answers = askUsual()
        langId = answers['language']
        language = LANGUAGES[langId]
        datatype_from_user = get_datatype_from_user(language_id=langId, filename='Types.json')
        args = ''
        templates_dict = dict({
            TARGET_FILE_FIELD: datatype_from_user.file_names[0],
            TARGET_METHOD_RETURN_FIELD: language.format_data(datatype_from_user.methods[0].return_type),
            TARGET_METHOD_FIELD: datatype_from_user.methods[0].method_name,
            TARGET_METHOD_ARGS_FIELD: args.join(map(lambda current: language.format_data(current), datatype_from_user.methods[0].method_parameters))
        })
        answers.update(templates_dict)
        langGen = LanguageGenerator(language, answers)
        langGen.create()
        commonEndingMessage(answers)

    # """Generate challenge from template."""
    #
    # def cpp(self):
    #     """ Generates a basic Cpp challenge """
    #     answers = askUsual()
    #     answers.update(askCppQuestions())
    #
    #     cppGen = LanguageGenerator(Cpp(), answers)
    #     cppGen.create()
    #
    #     commonEndingMessage(answers)
    #     pass
    #
    # def java(self):
    #     self.handle_langage_choice();
    #     """ Generates a basic C challenge """
    #     answers = askUsual()
    #     answers.update(askJavaQuestions())
    #
    #     language = Java()
    #     self.addTypeIfNecessary(self.parseTargetMethodArgs(answers['targetMethodArgs']), language)
    #
    #     javaGen = LanguageGenerator(language, answers)
    #     javaGen.create()
    #
    #     commonEndingMessage(answers)
    #     pass
    #
    # def addTypeIfNecessary(self, argTypes, language):
    #     commonTypes = ['byte', 'Byte', 'short', 'Short', 'int', 'Integer', 'float', 'Float', 'double', 'Double',
    #                    'String', 'long', 'Long', 'char', 'Character']
    #     for argType in argTypes:
    #         if argType not in commonTypes:
    #             language.addType(argType)
    #
    # def readTypes(self, fileName):
    #     loadedTypes = json.load(fileName)
    #     for currentType in loadedTypes:
    #         print(currentType)
    #
    # def parseTargetMethodArgs(self, args):
    #     return list(map(lambda s: s.strip().split(' ')[0], args.split(',')))
    #
    # def c(self):
    #     """ Generates a basic Java challenge """
    #     self.handle_langage_choice()
    #     pass
    #
    # def handle_langage_choice(self):
    #     answers = askUsual()
    #     answers.update(askCQuestions())
    #     cGen = LanguageGenerator(C(), answers)
    #     cGen.create()
    #     commonEndingMessage(answers)
    #
    # def python(self):
    #     """ Generates a basic Python challenge """
    #     answers = askUsual()
    #     answers.update(askPythonQuestions())
    #
    #     gen = LanguageGenerator(Python(), answers)
    #     gen.create()
    #
    #     commonEndingMessage(answers)
    #     pass
