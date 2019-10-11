#!/bin/bash
set -e
echo "Compiling java code"
cd src/main/java
javac -Xmaxerrs 1 app/*.java
echo "Executing code"
java -Xms32m -Xmx64m app/$1
echo "Done"