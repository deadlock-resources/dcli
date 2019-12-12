import fire
import os
import sys
from PyInquirer import prompt, print_json

from .questions.java import askJavaQuestions
from .questions.c import askCQuestions
from .questions.cpp import askCppQuestions 
from .questions.python import askPythonQuestions

from .logger import info, error, paragraph

from .generator import common, file
from .generator.languageGenerator import LanguageGenerator

from .language.java import Java
from .language.python import Python
from .language.c import C 
from .language.cpp import Cpp 


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

    ]
    answers = prompt(questions)
    if len(answers) == 0:
        error('Cancelled.')
        sys.exit()
    return answers


def commonEndingMessage(answers):
    info('You now have to complete many //TODO within the generated mission.')
    info('Then you will be able to test your mission with:')
    paragraph('dcli run ./' + answers['name'])
    paragraph('dcli solve ./' + answers['name'])


class Generator(object):
    """Generate challenge from template."""

    def cpp(self):
        """ Generates a basic Cpp challenge """
        answers = askUsual()
        answers.update(askCppQuestions())

        cppGen = LanguageGenerator(Cpp(), answers)
        cppGen.create()

        commonEndingMessage(answers)
        pass

    def java(self):
        """ Generates a basic C challenge """
        answers = askUsual()
        answers.update(askJavaQuestions())

        javaGen = LanguageGenerator(Java(), answers)
        javaGen.create()

        commonEndingMessage(answers)
        pass

    def c(self):
        """ Generates a basic Java challenge """
        answers = askUsual()
        answers.update(askCQuestions())

        cGen = LanguageGenerator(C(), answers)
        cGen.create()

        commonEndingMessage(answers)
        pass

    def python(self):
        """ Generates a basic Python challenge """
        answers = askUsual()
        answers.update(askPythonQuestions())

        gen = LanguageGenerator(Python(), answers)
        gen.create()

        commonEndingMessage(answers)
        pass

