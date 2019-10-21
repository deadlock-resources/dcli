import pkg_resources


def getPathFromTemplateDir(type, path):
    resource_path = '/'.join(('template', type + '/' + path))
    return pkg_resources.resource_filename('dcli', resource_path)


def loadFile(type, path):
    return open(getPathFromTemplateDir(type, path)).read()

def writeFile(path, content):
    newFile = open(path, "w+")
    newFile.write(content)
    newFile.close()

