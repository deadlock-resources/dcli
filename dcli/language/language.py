import os
import json
from .asset import Asset
from ..generator.file import open_file_from_root, get_path_from_root

DEFAULT_VALUE = 'defaultValue'
TYPE_NAME = 'name'

COMMON_TYPES_PATH = 'language/{}/types.json'

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
        path = str.format(COMMON_TYPES_PATH, self._type)
        if os.path.exists(get_path_from_root(path)) == True:
            json_content = open_file_from_root(path)
            return json.loads(json_content)
        else:
            return {}

    def contains_common_types(self):
        path = str.format(COMMON_TYPES_PATH, self._type)
        return os.path.exists(get_path_from_root(path))

    def is_common_type(self, current_type):
        return (not current_type or current_type in self._common_types)

    def get_default_value(self, current_type):
        # test empty String
        if not current_type:
            return ''
        elif self.is_common_type(current_type):
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

    def add_type_if_necessary(self, arg_types):
        for arg_type in arg_types:
            if not self.is_common_type(arg_type):
                self.add_type(arg_type)

    def parse_target_method_args(self, args, arg_type):
        return list(map(lambda s: s.strip().split(' ')[0], args.split(',')))

    def ask_questions(self): 
        raise NotImplementedError

    def need_to_generate_new_type(self):
        return True