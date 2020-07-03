from .language import Language

TEMPLATE_PATH = '/src/main/java/template'
SUCCESS_PATH = '/src/main/java/success'
APP_PATH = '/src/main/java/app'

SOLVE_PATH = '/src/main/java/app/Solve.java'
RUN_PATH = '/src/main/java/app/Run.java'

ASSET_PATHS = ['/src/main/java/app/Logger.java']

TARGET_FILE = 'Target'

class Java(Language):
    def __init__(self):
        Language.__init__(self,
            'java',
            TEMPLATE_PATH,
            SUCCESS_PATH,
            APP_PATH,
            SOLVE_PATH,
            RUN_PATH,
            TARGET_FILE,
            'java',
            ASSET_PATHS
        )

    
    def addType(self, name):
        self.addNewAsset(self.templateDirPath, name, f'package template;\n\nclass {name} {{}}')
        self.addNewAsset(self.successDirPath, name, f'package success;\n\nclass {name} {{}}')

