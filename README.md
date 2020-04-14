Tools to create, run your Deadlock challenges.

## Help
```bash
dcli --help
```

[Documentation about challenges.](https://deadlock-resources.github.io/challenge-documentation)

## Install from pip
```bash
pip install deadlock-cli --user
```
If it does not work make sure you have your PATH correctly set:  
`export PATH=$PATH:/home/$USER/.local/bin`

## Install from sources
```bash
git clone https://github.com/deadlock-resources/dcli.git
cd dcli/
pip3 install .
```
## Get dcli version
```bash
dcli version
```

## Generate mission
```bash
dcli gen (java|python|cpp|c|kotlin)
```

## Execute mission
```bash
dcli solve ./mission_path
dcli run ./mission_path
```
## Execute metamorph mission
To execute your multi language mission:
```bash
# running the Java code
dcli solve . java
dcli run . java

# running the Python code
dcli solve . python
dcli run . python
```

## Todo
* Add Haskell generator language


## Build archive from sources
```bash
python setup.py sdist
```

