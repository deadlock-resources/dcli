import pkg_resources

def loadChallengeYaml(type):
    """Return the content of challenge yaml file for the missionType asked

    >>> loadChallengeYaml(java)
    will returns the content of the challenge yaml file for Java.
    """
    return loadFile(type, '/challenge.yaml')

def getPathFromTemplateFile(type, path):
    resource_path = '/'.join(('template', type + '/' + path))
    return pkg_resources.resource_filename('dcli', resource_path)


def loadFile(type, path):
    return open(getPathFromTemplateFile(type, path)).read()

def writeFile(path, content):
    newFile = open(path, "w+")
    newFile.write(content)
    newFile.close()

