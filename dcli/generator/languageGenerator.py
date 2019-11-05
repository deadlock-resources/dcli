import os
from .common import template
from .file import loadFile, writeFile, getPathFromTemplateDir
from ..const import TARGET_FILE_FIELD, TARGET_METHOD_FIELD
from ..logger import info, error, jump
from colored import fg, attr
from shutil import copyfile

class LanguageGenerator():

    def __init__(self, language, answers):
        self._language = language
        self._root = answers['name']
        self._answers = answers

    def create(self):
        jump()
        info('Creating ' + self._language.type + ' challenge in ' + fg(208) + './' + self._root + '.')
        jump()
        self.createFolders()
        self.generateChallengeYaml()
        self.generateTemplateFile()
        self.generateSuccessFile()
        self.generateSolveFile()
        self.generateRunFile()
        self.generateDocs()
        self.copyCommonFiles()
        self.copyAssets()

        info('Challenge ' + self._root + ' created with success!')
    
    def copyAssets(self):
        for asset in self._language.assets:
            self.templateAndCopyFile(asset)

    def generateChallengeYaml(self):
        self.templateAndCopyFile('/challenge.yaml')

    def copyCommonFiles(self):
        self.copyFile('Dockerfile')
        self.copyFile('run.sh')
        self.copyFile('thumbnail.png')

    def templateAndCopyFile(self, file):
        writeFile(self._root + '/' + file, template(self._answers, loadFile(self._language.type, file)))

    def copyFile(self, file):
        copyfile(getPathFromTemplateDir(self._language.type, file), self._root + '/' + file)


    def createFolders(self):
        os.makedirs(self._root + '/docs/fr', exist_ok=True)
        os.makedirs(self._root + self._language.appDirPath, exist_ok=True)
        os.makedirs(self._root + self._language.templateDirPath, exist_ok=True)
        os.makedirs(self._root + self._language.successDirPath, exist_ok=True)

    def generateTemplateFile(self):
        fileName = self.getTargetFilePath(self._language.templateDirPath, self.getTargetFileName())
        writeFile(fileName, template(self._answers, loadFile(self._language.type, self._language.getPathToTemplateTargetFile())))


    def generateSuccessFile(self):
        fileName = self.getTargetFilePath(self._language.successDirPath, self.getTargetFileName())
        writeFile(fileName, template(self._answers, loadFile(self._language.type, self._language.getPathToSuccessTargetFile())))


    def generateSolveFile(self):
        fileName = self._root + self._language.solvePath
        writeFile(fileName, template(self._answers, loadFile(self._language.type, self._language.solvePath)))


    def generateRunFile(self):
        fileName = self._root + self._language.runPath
        writeFile(fileName, template(self._answers, loadFile(self._language.type, self._language.runPath)))

    def generateDocs(self):
        self.templateAndCopyFile('/docs/briefing.md')
        self.templateAndCopyFile('/docs/fr/briefing.md')

    def getTargetFilePath(self, path, file):
        return self._root + path + '/' + file + '.' + self._language.extension

    def getTargetFileName(self):
        if TARGET_FILE_FIELD in self._answers:
            return self._answers[TARGET_FILE_FIELD]
        return self._language.targetFile
