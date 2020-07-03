from jinja2 import Template
from .file import write_file


def template(context, template):
    """Replace all var in template by the given context
    """
    return Template(template).render(context)
