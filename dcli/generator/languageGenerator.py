import os
from .common import template
from .file import loadFile, writeFile
from ..const import TARGET_FILE_FIELD, TARGET_METHOD_FIELD
from ..logger import info, error, jump
from colored import fg, attr

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
        self.generateTemplateFile()
        self.generateSuccessFile()
        self.generateSolveFile()
        self.generateTestFile()
        self.generateDocs()

        info('Challenge ' + self._root + ' created with success!')

    def createFolders(self):
        os.makedirs(self._root + '/docs', exist_ok=True)
        os.makedirs(self._root + self._language.appDirPath, exist_ok=True)
        os.makedirs(self._root + self._language.templateDirPath, exist_ok=True)
        os.makedirs(self._root + self._language.successDirPath, exist_ok=True)

    def generateTemplateFile(self):
        fileName = self.getTargetFilePath(self._language.templateDirPath, self._answers[TARGET_FILE_FIELD])
        writeFile(fileName, template(self._answers, loadFile(self._language.type, self._language.getPathToTemplateTargetFile())))


    def generateSuccessFile(self):
        fileName = self.getTargetFilePath(self._language.successDirPath, self._answers[TARGET_FILE_FIELD])
        writeFile(fileName, template(self._answers, loadFile(self._language.type, self._language.getPathToSuccessTargetFile())))


    def generateSolveFile(self):
        fileName = self._root + self._language.solvePath
        writeFile(fileName, template(self._answers, loadFile(self._language.type, self._language.solvePath)))


    def generateTestFile(self):
        fileName = self._root + self._language.testPath
        writeFile(fileName, template(self._answers, loadFile(self._language.type, self._language.testPath)))

    def generateDocs(self):
        fileName = self._root + '/docs/briefing.md'
        writeFile(fileName, template(self._answers, loadFile(self._language.type, 'docs/briefing.md')))

        fileName = self._root + '/docs/fr/briefing.md'
        writeFile(fileName, template(self._answers, loadFile(self._language.type, 'docs/fr/briefing.md')))

    def getTargetFilePath(self, path, file):
        return self._root + path + '/' + file + '.' + self._language._extension
