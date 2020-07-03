
## UNRELEASED

## 1.1.5 (23/04/2020)
* fix load common types when non present
* check challenge yaml file before loading it

## 1.1.4 (22/04/2020)
* fix(gen) broken when common types was missing

## 1.1.3 (15/04/2020)
* fix(c) missing ; and bool include
* fix(java) list default types
* feat(cpp) support for empty return field
* feat(java) support for default return value
* refactor function naming rules

## 1.1.1 (15/04/2020)
* fix way to quiet command line, improve os compatibility

## 1.1.0 (29/03/2020)
* improve run|solve logs
* fix spinner broken pipe
* add support for multi service challenge

## 1.0.01 (10/03/2020)
* fix use custom tmp dir to execute metamorph mission

## 1.0.0 (10/03/2020)
* finally first release
* improve running metamorph mission with docker volume, to avoid building image everytime, and improve performance

## 0.0.99 (09/03/2020)
* fix sping error when build fail
* create docker env to run|solve metamorph challenge instead of using host binary
* better logs when error happens to run metamorph mission

## 0.0.98 (27/02/2020)
* fix missing pyyaml dependency

## 0.0.97 (26/02/2020)
* auto generating class when unknow type are given for `dcli gen java`
* support to run|solve metamorph challenge (Linux support)
 
## 0.0.96 (17/01/2020)
* improve runner logs and spinner
* give more feedback when building image fail
* run build script before building Docker image
