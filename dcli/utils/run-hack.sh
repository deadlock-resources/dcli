#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
. $DIR/parse_yaml.sh

CANDIDATE_ID=$(uuidgen)
PORT=9090
CONTAINER_NAME="hack_test"
DEADLOCK_TOKEN_TMP="/tmp/deadlock/token"

eval $(parse_yaml "$(pwd)/challenge.yaml" "challenge_")

if [[ ! -e $DEADLOCK_TOKEN_TMP ]]; then
    echo "> create tmp dir.."
    mkdir -p $DEADLOCK_TOKEN_TMP
fi
echo "> create tmp token.."
echo $(uuidgen) > $DEADLOCK_TOKEN_TMP/$CANDIDATE_ID.token

COUNT=$(docker ps -a | grep "$CONTAINER_NAME" | wc -l)
if (($COUNT > 0)); then
    echo "> stop previous container"
    docker rm $CONTAINER_NAME -f
fi

echo "> building challenge.."
docker build $(pwd) -q -t hack
echo "> starting challenge.."
docker run -v $DEADLOCK_TOKEN_TMP:$challenge_hacking_token_path -d -p $PORT:80 --name $CONTAINER_NAME hack 
echo "-------------------------------------------------------------------------------------------------------------------------"
echo "> hack challenge is ready under http://localhost:$PORT$challenge_hacking_index"
echo "-------------------------------------------------------------------------------------------------------------------------"