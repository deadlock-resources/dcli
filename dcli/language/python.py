from .language import Language

TEMPLATE_PATH = '/src/main/python/template'
SUCCESS_PATH = '/src/main/python/success'
APP_PATH = '/src/main/python/app'

SOLVE_PATH = '/src/main/python/Solve.py'
TEST_PATH = '/src/main/python/Test.py'

TARGET_FILE = '__init__.py'

class Python(Language):
    def __init__(self):
        Language.__init__(self,
            'python',
            TEMPLATE_PATH,
            SUCCESS_PATH,
            APP_PATH,
            SOLVE_PATH,
            TEST_PATH,
            TARGET_FILE,
            'py'
        )

