import pkg_resources
import yaml
import io
import tempfile

def create_tmp_folder():
    return tempfile.mkdtemp()

def get_path_from_root(path):
    return pkg_resources.resource_filename('dcli', '/' + path)

def get_path_from_template_dir(type, path):
    resource_path = '/'.join(('template', type + '/' + path))
    return pkg_resources.resource_filename('dcli', resource_path)

def load_yaml(path):
    with open(path, 'r') as stream:
        return yaml.safe_load(stream)

def open_file_from_root(path):
    return open(get_path_from_root(path)).read()

def open_file_from_template_dir(type, path):
    return open(get_path_from_template_dir(type, path)).read()

def write_file(path, content):
    newFile = open(path, "w+")
    newFile.write(content)
    newFile.close()

