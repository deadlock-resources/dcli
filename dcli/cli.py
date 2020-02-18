#! python3
import fire
import pkg_resources  # part of setuptools

from .generatorCli import Generator
from .runner import run, solve


def version():
    return pkg_resources.require("deadlock-cli")[0].version


def gen_without_type():
    Generator().generate()


def gen_with_type(l=''):
    if l == '':
        gen_without_type()
    else:
        print('type is ' + l)
        Generator().handle_gen_for_language(l)


def main():
    fire.Fire({
        'version': version,
        'gen': gen_with_type,
        'solve': solve,
        'run': run,
    })


if __name__ == '__main__':
    main()
