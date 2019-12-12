from .language import Language

TEMPLATE_PATH = '/src/template'
SUCCESS_PATH = '/src/success'
APP_PATH = '/src/app'

SOLVE_PATH = '/src/app/main.c'
RUN_PATH = '/src/app/main.c'

ASSETS = ['src/Makefile', 'src/template/Target.h', 'src/app/Logger.c', 'src/app/Logger.h']

TARGET_FILE = 'Target'

class C(Language):
    def __init__(self):
        Language.__init__(self,
            'c',
            TEMPLATE_PATH,
            SUCCESS_PATH,
            APP_PATH,
            SOLVE_PATH,
            RUN_PATH,
            TARGET_FILE,
            'c',
            ASSETS
        )
