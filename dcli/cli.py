#! python3
import os
import fire
import inquirer
import subprocess

from .generatorCli import Generator
from .logger import info
from .runner import run, solve
from .spinCursor import SpinCursor
import time


def main():
  fire.Fire({
    'gen': Generator(),
    'solve': solve,
    'run': run
  })


if __name__ == '__main__':
  main()
