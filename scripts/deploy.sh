#!/bin/sh

python3 -m pip install --upgrade pip setuptools wheel --user
python3 -m pip install twine --user

python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
