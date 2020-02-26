
## UNRELEASED
* add resources for primitive types through json files
* creates types_helper.py file, that uses inquirer lib in order to collect, method return types, arguments name and type
* handle generics for java and cpp
* handle default return value when code generates
* language can be selected by user if not specified in command line, then it can be selected through inquirer list of choice
* fix spin error when build fail
* create docker env to run|solve metamorph challenge instead of using host binary

## 0.0.98 (27/02/2020)
* fix missing pyyaml dependency

## 0.0.97 (26/02/2020)
* auto generating class when unknow type are given for `dcli gen java`
* support to run|solve metamorph challenge (Linux support)

## 0.0.96 (17/01/2020)
* improve runner logs and spinner
* give more feedback when building image fail
* run build script before building Docker image
