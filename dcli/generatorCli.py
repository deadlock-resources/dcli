import fire
import os
from PyInquirer import prompt, print_json
from .logger import info
from .generator import java, common, file


def askUsual():
    questions = [
        {
            'type': 'input',
            'name': 'name',
            'message': 'Name (code_your_challenge_name):',
        },
        {
            'type': 'input',
            'name': 'label',
            'message': 'Label (Challenge name):',
        },
        {
            'type': 'input',
            'name': 'description',
            'message': 'Description:',
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
    return prompt(questions)


class Generator(object):
    """Generate challenge from template."""

    def java(self):
        javaQuestions = [
            {
                'type': 'input',
                'name': 'targetFile',
                'message': 'Main file for the user (Main.java):',
            },
            {
                'type': 'input',
                'name': 'targetMethod',
                'message': 'Main method for the user (String method(int a)):',
            },
        ]
        answers = askUsual()
        answers.update(prompt(javaQuestions))

        info('Create folder')
        folderName = answers['name'].strip()
        os.mkdir(folderName)
        info('Create descriptor')
        file.writeFile(folderName + '/challenge.yml', common.template(answers, file.loadChallengeYaml('java')))

        return ''


def python(self):
    print('Hello Python')
