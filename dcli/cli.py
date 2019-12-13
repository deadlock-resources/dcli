#! python3
import os
import fire
import subprocess
import pkg_resources  # part of setuptools

from .generatorCli import Generator
from .logger import info
from .runner import run, solve
from .spinCursor import SpinCursor
import time

def version():
  return pkg_resources.require("deadlock-cli")[0].version

def main():
  fire.Fire({
    'version': version,
    'gen': Generator(),
    'solve': solve,
    'run': run,
  })


if __name__ == '__main__':
  main()
