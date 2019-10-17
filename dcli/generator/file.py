import pkg_resources

def loadChallengeYaml(type):
    """Return the content of challenge yaml file for the missionType asked

    >>> loadChallengeYaml(java)
    will returns the content of the challenge yaml file for Java.
    """
    return loadFile(type, '/challenge.yaml')


def loadFile(type, path):
    resource_path = '/'.join(('template', type + '/' + path))
    return open(pkg_resources.resource_filename('dcli', resource_path)).read()

def writeFile(path, content):
    newFile = open(path, "w+")
    newFile.write(content)
    newFile.close()

