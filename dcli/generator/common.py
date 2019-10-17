from jinja2 import Template
from .file import writeFile, loadChallengeYaml


def generateTemplate(type, root, answers):
    writeFile(root + '/challenge.yml', template(answers, loadChallengeYaml(type)))


def template(context, template):
    """Replace all var in template by the given context
    """
    return Template(template).render(context)
