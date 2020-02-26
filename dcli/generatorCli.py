import sys

from PyInquirer import prompt

from .const import TARGET_METHOD_FIELD, TARGET_METHOD_RETURN_FIELD, TARGET_METHOD_ARGS_FIELD, TARGET_FILE_FIELD, \
    TARGET_DEFAULT_RETURN_FIELD, TARGET_GENERICS_FIELD
from .generator.languageGenerator import LanguageGenerator
from .language.c import C
from .language.cpp import Cpp
from .language.java import Java
from .language.python import Python
from .language.types_helper import FormAnswersCollector
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
        'choices':
            LANGUAGES.keys()
        ,
    }

    answers = prompt(question)
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

    # def cpp(self):

    def generate(self):
        langId = askLanguage()['language']
        self.handle_gen_for_language(langId)

    def handle_gen_for_language(self, langId):
        answers = askUsual()
        language = LANGUAGES[langId]
        datatype_from_user = FormAnswersCollector(language_id=langId, filename='Types.json',
                                                  allow_type_creation=language.allow_type_creation,
                                                  allow_typing=language.allow_strong_typing).structure_holder
        # for now only handle one single method
        templates_dict = dict({
            TARGET_GENERICS_FIELD: ', '.join(
                map(lambda current: language.format_generic_declaration(str(current)),
                    datatype_from_user.methods[0].get_generics_types())),
            TARGET_FILE_FIELD: datatype_from_user.file_names[0],
            TARGET_METHOD_RETURN_FIELD: language.format_data(datatype_from_user.methods[0].return_type),
            TARGET_DEFAULT_RETURN_FIELD: datatype_from_user.methods[0].return_type.default_value,
            TARGET_METHOD_FIELD: datatype_from_user.methods[0].method_name,
            TARGET_METHOD_ARGS_FIELD: ','.join(
                map(lambda current: language.format_data(current), datatype_from_user.methods[0].method_parameters))
        })
        answers.update(templates_dict)
        langGen = LanguageGenerator(language, answers)
        langGen.create()
        commonEndingMessage(answers)
