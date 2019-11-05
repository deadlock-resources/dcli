from .language import Language

TEMPLATE_PATH = '/src/main/python/template'
SUCCESS_PATH = '/src/main/python/success'
APP_PATH = '/src/main/python/app'

SOLVE_PATH = '/src/main/python/Solve.py'
RUN_PATH = '/src/main/python/Run.py'

TARGET_FILE = '__init__'

class Python(Language):
    def __init__(self):
        Language.__init__(self,
            'python',
            TEMPLATE_PATH,
            SUCCESS_PATH,
            APP_PATH,
            SOLVE_PATH,
            RUN_PATH,
            TARGET_FILE,
            'py'
        )

