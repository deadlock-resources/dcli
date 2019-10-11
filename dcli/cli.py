#! python3
import os
import fire
import inquirer
import subprocess

from string import Template
from .generatorCli import Generator

class Cli(object):
  """Deadlock CLI."""

  def __init__(self):
    self.gen = Generator()


def main():
  fire.Fire(Cli)

if __name__ == '__main__':
  main()
