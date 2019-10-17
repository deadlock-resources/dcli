import pkg_resources

def loadChallengeYaml(missionType):
    """Return the content of challenge yaml file for the missionType asked

    >>> loadChallengeYaml(java)
    will returns the content of the challenge yaml file for Java.
    """
    resource_path = '/'.join(('template', missionType + '/challenge.yaml'))
    return open(pkg_resources.resource_filename('dcli', resource_path)).read()
    # return pkg_resources.resource_string('dcli', resource_path)


def writeFile(path, content):
    newFile = open(path, "w+")
    newFile.write(content)
    newFile.close()

