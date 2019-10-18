#! python3
import os
import fire
import inquirer
import subprocess

from .runner import Runner
from .generatorCli import Generator
from .logger import info

class Cli(object):
  """Deadlock CLI."""

  def __init__(self):
    self.gen = Generator()


def main():
  fire.Fire(Cli)
  # fire.Fire(Runner)

if __name__ == '__main__':
  main()
