import fire
import os
import sys
from PyInquirer import prompt, print_json

from .language.java.question import askJavaQuestions
from .language.c.question import askCQuestions
from .language.cpp.question import askCppQuestions 
from .language.python.question import askPythonQuestions

from .logger import info, error, paragraph

from .generator import common, file
from .generator.languageGenerator import LanguageGenerator

from .language.java import Java
from .language.python import Python
from .language.c import C 
from .language.cpp import Cpp 

from .const import TARGET_METHOD_RETURN_VALUE


def ask_usual():
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

    ]
    answers = prompt(questions)
    if len(answers) == 0:
        error('Cancelled.')
        sys.exit()
    return answers


def common_end_message(answers):
    info('You have to complete many //TODO within the generated mission.')
    info('Then you will be able to test your mission with:')
    paragraph('dcli run ./' + answers['name'])
    paragraph('dcli solve ./' + answers['name'])


class Generator(object):
    """Generate challenge from template."""

    def cpp(self):
        """ Generates a basic Cpp challenge """
        answers = ask_usual()
        answers.update(askCppQuestions())

        cppGen = LanguageGenerator(Cpp(), answers)
        cppGen.create()

        common_end_message(answers)
        pass

    def java(self):
        """ Generates a basic C challenge """
        answers = ask_usual()
        answers.update(askJavaQuestions())

        language = Java()
        self.add_type_if_necessary(self.parse_target_method_args(answers['targetMethodArgs']), language)
        self.add_type_if_necessary(self.parse_target_method_args(answers['targetMethodReturn']), language)

        # append default value
        answers[TARGET_METHOD_RETURN_VALUE] = language.get_default_value(answers['targetMethodReturn'])

        javaGen = LanguageGenerator(language, answers)
        javaGen.create()

        common_end_message(answers)
        pass

    def add_type_if_necessary(self, arg_types, language):
        for arg_type in arg_types:
            if not language.is_common_type(arg_type):
                language.add_type(arg_type)

    def parse_target_method_args(self, args):
        return list(map(lambda s: s.strip().split(' ')[0], args.split(',')))


    def c(self):
        """ Generates a basic Java challenge """
        answers = ask_usual()
        answers.update(askCQuestions())

        cGen = LanguageGenerator(C(), answers)
        cGen.create()

        common_end_message(answers)
        pass

    def python(self):
        """ Generates a basic Python challenge """
        answers = ask_usual()
        answers.update(askPythonQuestions())

        gen = LanguageGenerator(Python(), answers)
        gen.create()

        common_end_message(answers)
        pass

