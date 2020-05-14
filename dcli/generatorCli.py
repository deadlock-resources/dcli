import fire
import os
import sys
from PyInquirer import prompt

from .logger import info, error, paragraph

from .generator import common, file
from .generator.languageGenerator import LanguageGenerator

from .language.java import Java
from .language.python import Python
from .language.c import C 
from .language.cpp import Cpp 
from .language.kotlin import Kotlin

from .const import TARGET_METHOD_RETURN_VALUE, TARGET_METHOD_RETURN_FIELD, TARGET_METHOD_ARGS_FIELD 

NOT_BE_EMPTY = 'Must not be empty.'

LANGUAGES = dict({
    'java': Java(),
    'cpp': Cpp(),
    'c': C(),
    'python': Python(),
    'kotlin': Kotlin()
})

def ask_usual():
    questions = [
        {
            'type': 'input',
            'name': 'name',
            'message': 'Name (e.g. code_your_challenge_name):',
            'validate': lambda text: len(text) > 0 or NOT_BE_EMPTY
        },
        {
            'type': 'input',
            'name': 'label',
            'message': 'Title (e.g. Building rockets)',
            'validate': lambda text: len(text) > 0 or NOT_BE_EMPTY
        },
        {
            'type': 'input',
            'name': 'description',
            'message': 'Description (e.g. Challenge to learn building rockets and save the world!):',
            'validate': lambda text: len(text) > 0 or NOT_BE_EMPTY
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

def askLanguage():
    question = {
        'type': 'list',
        'name': 'language',
        'message': 'Choose your language',
        'choices': LANGUAGES.keys(),
    }
    answers = prompt(question)
    if len(answers) == 0:
        error('Cancelled.')
        sys.exit()
    return answers

def common_end_message(answers):
    info('You have to complete many //TODO within the generated mission.')
    info('Then you will be able to test your mission with:')
    paragraph('dcli run ./' + answers['name'])
    paragraph('dcli solve ./' + answers['name'])

def generate_for_language(langId):
    if langId not in LANGUAGES:
        error('You have to specify a language belonging to the following list: %s' % list(LANGUAGES.keys()))
        sys.exit(1)

    language = LANGUAGES[langId]
    answers = ask_usual()
    answers.update(language.ask_questions())

    if language.need_to_generate_new_type(): 
        language.add_type_if_necessary(language.parse_target_method_args(answers[TARGET_METHOD_ARGS_FIELD], TARGET_METHOD_ARGS_FIELD))
        language.add_type_if_necessary(language.parse_target_method_args(answers[TARGET_METHOD_RETURN_FIELD], TARGET_METHOD_RETURN_FIELD))
        # append default value
        answers[TARGET_METHOD_RETURN_VALUE] = language.get_default_value(answers[TARGET_METHOD_RETURN_FIELD])
    langGen = LanguageGenerator(language, answers)
    langGen.create()

    common_end_message(answers)

class Generator():

    def generate(self):
        langId = askLanguage()["language"]
        generate_for_language(langId)