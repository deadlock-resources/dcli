#! python3
import os

import fire
import pkg_resources  # part of setuptools

from .generatorCli import Generator, generate_for_language
from .runner import run, solve, download_if_necessary

def version():
  return pkg_resources.require("deadlock-cli")[0].version

def gen_without_type():
  Generator().generate()

def gen_with_type(l=''):
  if l == '':
    gen_without_type()
  else:
    generate_for_language(l)

def build(path=os.getcwd()):
    download_if_necessary(path);

def main():
  fire.Fire({
    'version': version,
    'gen': gen_with_type,
    'solve': solve,
    'run': run,
    'build': build,
  })


if __name__ == '__main__':
  main()
