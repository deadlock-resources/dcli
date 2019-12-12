#!/bin/bash
set -e
echo "Compiling C code"
make --quiet
./app $1
echo "Done"
