#! python3
import os
import fire
import inquirer
import subprocess

from .generatorCli import Generator
from .logger import info
from .runner import run, solve

def main():
  fire.Fire({
    'gen': Generator(),
    'solve': solve,
    'run': run
  })

if __name__ == '__main__':
  main()
