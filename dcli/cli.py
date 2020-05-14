#! python3
import os
import fire
import subprocess
import pkg_resources  # part of setuptools

from .generatorCli import Generator, generate_for_language
from .logger import info
from .runner import run, solve
from .spinCursor import SpinCursor
import time

def version():
  return pkg_resources.require("deadlock-cli")[0].version

def gen_without_type():
  Generator().generate()

def gen_with_type(l=''):
  if l == '':
    gen_without_type()
  else:
    generate_for_language(l)

def main():
  fire.Fire({
    'version': version,
    'gen': gen_with_type,
    'solve': solve,
    'run': run,
  })


if __name__ == '__main__':
  main()
