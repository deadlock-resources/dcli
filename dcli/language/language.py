import json
from .asset import Asset
from ..generator.file import open_file_from_root

DEFAULT_VALUE = 'defaultValue'
TYPE_NAME = 'name'

class LanguageType:
    def __init__(self, name='', default_value=None):
        self.default_value = default_value
        self.name = name

class Language():

    def __init__(self,
                type,
                templateDirPath,
                successDirPath,
                appDirPath,
                solvePath,
                runPath,
                targetDefaultFile,
                extension,
                assetsPaths = []):
        """ Default value for Language class """
        self._type = type
        self._templateDirPath = templateDirPath
        self._successDirPath = successDirPath
        self._appDirPath = appDirPath
        self._solvePath = solvePath
        self._runPath = runPath
        self._targetDefaultFile = targetDefaultFile
        self._extension = extension
        self._assetPaths = assetsPaths
        self._newAssets = []
        self._common_types = self.load_common_types()

    @property
    def assetPaths(self):
        return self._assetPaths

    @property
    def newAssets(self):
        return self._newAssets

    @property
    def extension(self):
        return self._extension

    @property
    def type(self):
        return self._type

    @property
    def appDirPath(self):
        return self._appDirPath

    @property
    def templateDirPath(self):
        return self._templateDirPath

    @property
    def successDirPath(self):
        return self._successDirPath

    @property
    def solvePath(self):
        return self._solvePath

    @property
    def runPath(self):
        return self._runPath

    @property
    def targetFile(self):
        return self._targetDefaultFile

    @property
    def common_types(self):
        return self._common_types

    def load_common_types(self):
        json_content = open_file_from_root(f'language/{self._type}/types.json')
        return json.loads(json_content)

    def is_common_type(self, current_type):
        return (not current_type or current_type in self._common_types)

    def get_default_value(self, current_type):
        if self.is_common_type(current_type):
            return self._common_types[current_type][DEFAULT_VALUE]
        else:
            return 'null'

    def add_type(self, name):
        self.add_new_asset(self.templateDirPath, name, f'class {name} {{}}')
        self.add_new_asset(self.successDirPath, name, f'class {name} {{}}')

    def get_path_to_template_target_file(self):
        return self.templateDirPath + '/' + self.targetFile + '.' + self.extension
    
    def get_path_to_success_target_file(self):
        return self.successDirPath + '/' + self.targetFile + '.' + self.extension

    def add_new_asset(self, assetPath, assetFileName, assetContent):
        self._newAssets.append(Asset(assetPath, assetFileName, assetContent))