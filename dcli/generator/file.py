import pkg_resources
import yaml
import io
import tempfile

def createTmpFolder():
    return tempfile.mkdtemp()

def getPathFromRoot(path):
    return pkg_resources.resource_filename('dcli', '/' + path)

def getPathFromTemplateDir(type, path):
    resource_path = '/'.join(('template', type + '/' + path))
    return pkg_resources.resource_filename('dcli', resource_path)

def loadYaml(path):
    with open(path, 'r') as stream:
        return yaml.safe_load(stream)


def loadFile(type, path):
    return open(getPathFromTemplateDir(type, path)).read()

def writeFile(path, content):
    newFile = open(path, "w+")
    newFile.write(content)
    newFile.close()

