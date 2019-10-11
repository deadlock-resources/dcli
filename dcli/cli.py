#! python3
from . import template  # relative-import the *package* containing the templates
import os
import fire
import inquirer
import subprocess

from string import Template
from .generator import Generator
import pkg_resources

class Cli(object):
  """Deadlock CLI."""

  def __init__(self):
    self.gen = Generator()


def main():
  # Could be any dot-separated package/module name or a "Requirement"
  resource_package = __name__
  resource_path = '/'.join(('template', 'java/challenge.yaml'))  # Do not use os.path.join()
  template = pkg_resources.resource_string(resource_package, resource_path)
  print(template)
  fire.Fire(Cli)

if __name__ == '__main__':
  main()
