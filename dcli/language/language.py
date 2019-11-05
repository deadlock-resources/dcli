
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
                assets = []):
        """ Default value for Language class """
        self._type = type
        self._templateDirPath = templateDirPath
        self._successDirPath = successDirPath
        self._appDirPath = appDirPath
        self._solvePath = solvePath
        self._runPath = runPath
        self._targetDefaultFile = targetDefaultFile
        self._extension = extension
        self._assets = assets

    @property
    def assets(self):
        return self._assets

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
    