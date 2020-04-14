from ..language import Language

TEMPLATE_PATH = '/src/main/kotlin/template'
SUCCESS_PATH = '/src/main/kotlin/success'
APP_PATH = '/src/main/kotlin/app'

SOLVE_PATH = '/src/main/kotlin/app/Solve.kt'
RUN_PATH = '/src/main/kotlin/app/Run.kt'

ASSET_PATHS = ['/src/main/kotlin/app/Logger.kt', '/src/main/kotlin/app/Main.kt']

TARGET_FILE = 'Target'

class Kotlin(Language):
    def __init__(self):
        Language.__init__(self,
            'kotlin',
            TEMPLATE_PATH,
            SUCCESS_PATH,
            APP_PATH,
            SOLVE_PATH,
            RUN_PATH,
            TARGET_FILE,
            'kt',
            ASSET_PATHS
        )

    def add_type(self, name):
        self.add_new_asset(self.templateDirPath, name, f'package template\n\nclass {name} {{}}')
        self.add_new_asset(self.successDirPath, name, f'package success\n\nclass {name} {{}}')

