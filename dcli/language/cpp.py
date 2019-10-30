from .language import Language

TEMPLATE_PATH = '/src/template'
SUCCESS_PATH = '/src/success'
APP_PATH = '/src/app'

SOLVE_PATH = '/src/app/main.cpp'
TEST_PATH = '/src/app/main.cpp'

ASSETS = ['src/Makefile', 'src/template/Target.h', 'src/app/Logger.cpp', 'src/app/Logger.h']

TARGET_FILE = 'Target'

class Cpp(Language):
    def __init__(self):
        Language.__init__(self,
            'cpp',
            TEMPLATE_PATH,
            SUCCESS_PATH,
            APP_PATH,
            SOLVE_PATH,
            TEST_PATH,
            TARGET_FILE,
            'cpp',
            ASSETS
        )
