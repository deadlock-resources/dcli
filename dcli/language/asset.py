class Asset():

    def __init__(self, path, fileName, content, extension):
        self._path = path
        self._fileName = fileName
        self._content = content
        self._extension = extension

    @property
    def path(self):
        return self._path

    @property
    def fileName(self):
        return self._fileName

    @property
    def content(self):
        return self._content

    @property
    def extension(self):
        return self._extension