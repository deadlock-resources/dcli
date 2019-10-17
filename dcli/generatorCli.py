import fire
import os
import sys
from PyInquirer import prompt, print_json
from .questions.java import askJavaQuestions
from .logger import info, error
from .generator import common, file
from .generator.languageGenerator import LanguageGenerator
from .language.java import Java


def askUsual():
    questions = [
        {
            'type': 'input',
            'name': 'name',
            'message': 'Name (e.g. code_your_challenge_name):',
            'validate': lambda text: len(text) > 0 or 'Must not be empty'
        },
        {
            'type': 'input',
            'name': 'label',
            'message': 'Label (e.g Challenge name):',
            'validate': lambda text: len(text) > 0 or 'Must not be empty'
        },
        {
            'type': 'input',
            'name': 'description',
            'message': 'Description:',
            'validate': lambda text: len(text) > 0 or 'Must not be empty'
        },
        {
            'type': 'list',
            'name': 'level',
            'message': 'Level (easiest to hardest):',
            'choices': [
                'jajarbinks', 'ewok', 'padawan', 'jedi', 'master'
            ],
        },

    ]
    answers = prompt(questions)
    if len(answers) == 0:
        error('Cancelled.')
        sys.exit()
    return answers


class Generator(object):
    """Generate challenge from template."""

    def java(self):
        answers = askUsual()
        answers.update(askJavaQuestions())

        javaGen = LanguageGenerator(Java(), answers)
        javaGen.create()

        return ''

