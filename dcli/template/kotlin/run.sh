#!/bin/bash
set -e
echo "Compiling kotlin code"
cd src/main/kotlin
kotlinc app/*.kt template/*.kt success/*.kt -include-runtime -d challenge.jar
echo "Executing code"
java -jar -Xms32m -Xmx64m challenge.jar $1
echo "Done"