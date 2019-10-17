#!/bin/bash
set -e
echo "Compiling python code"
cd src/main/python
python -m py_compile *.py
echo "Executing code"
python $1.py
echo "Done"
