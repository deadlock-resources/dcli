from .language import Language

TEMPLATE_PATH = '/src/main/java/template'
SUCCESS_PATH = '/src/main/java/success'
APP_PATH = '/src/main/java/app'

SOLVE_PATH = '/src/main/java/app/Solve.java'
TEST_PATH = '/src/main/java/app/Test.java'

ASSETS = ['/src/main/java/app/Logger.java']

TARGET_FILE = 'Target'

class Java(Language):
    def __init__(self):
        Language.__init__(self,
            'java',
            TEMPLATE_PATH,
            SUCCESS_PATH,
            APP_PATH,
            SOLVE_PATH,
            TEST_PATH,
            TARGET_FILE,
            'java',
            ASSETS
        )
