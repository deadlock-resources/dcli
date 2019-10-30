#!/bin/bash
set -e
echo "Compiling C++ code"
make --quiet
echo "Running"
./app $1
echo "Done"
