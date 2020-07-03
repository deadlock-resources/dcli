#! python3
import os
import json
import urllib.request

import fire
import pkg_resources  # part of setuptools
from distutils.version import StrictVersion

from .generatorCli import Generator, generate_for_language
from .runner import run, solve, download_if_necessary

from .logger import info
from colored import fg, bg, attr

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
    download_if_necessary(path)

def last_version():
    url = "https://pypi.org/pypi/deadlock-cli/json"
    with urllib.request.urlopen(url) as response:
      data = json.loads(response.read())
      versionKeys = data["releases"].keys()
      versionsList = list(versionKeys)
      return versionsList[-1]

def warning_if_outdated():
  last = last_version()
  current = version()
  if (last != current):
    info(f'{attr(5)}New version available{attr(0)} [{fg(1)}{current}{attr(0)}{attr("bold")} ' +
         f'-> {fg(2)}{last}{attr(0)}{attr("bold")}], ' +
         f'run "pip install deadlock-cli --upgrade" to upgrade.')


def main():
  warning_if_outdated()
  fire.Fire({
    'version': version,
    'gen': gen_with_type,
    'solve': solve,
    'run': run,
    'build': build,
  })


if __name__ == '__main__':
  main()
