#!/bin/sh

# copy everything from tmp runner dir to avoid any right problem
cp -r /tmp/runner/. /opt/runner

./runner $1 $2