from .asset import Asset


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
                 assetsPaths=[],
                 allow_strong_typing=True,
                 allow_type_creation=False):
        """ Default value for Language class """
        self.allow_type_creation = allow_type_creation
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
        self._allow_strong_typing = allow_strong_typing

    @property
    def assetPaths(self):
        return self._assetPaths

    @property
    def newAssets(self):
        return self._newAssets

    @property
    def allow_strong_typing(self):
        return self._allow_strong_typing

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

    def getPathToTemplateTargetFile(self):
        return self.templateDirPath + '/' + self.targetFile + '.' + self.extension

    def getPathToSuccessTargetFile(self):
        return self.successDirPath + '/' + self.targetFile + '.' + self.extension

    def addNewAsset(self, assetPath, assetFileName, assetContent):
        self._newAssets.append(Asset(assetPath, assetFileName, assetContent))

    def format_generic_declaration(self, type_name):
        return type_name
