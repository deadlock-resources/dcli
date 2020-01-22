class Asset():

    def __init__(self, path, fileName, content):
        self._path = path
        self._fileName = fileName
        self._content = content

    @property
    def path(self):
        return self._path

    @property
    def fileName(self):
        return self._fileName

    @property
    def content(self):
        return self._content