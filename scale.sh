#!/bin/bash

if [[ ! -n $1 ]];
then 
    echo "No parameter passed - up or down."
    exit
fi

COUNT=$(docker ps | grep whist-homework-backend | wc -l)

case "$1" in
up) 
    let "RESULT = $COUNT + 5"
    docker compose up --scale backend=$RESULT -d
    echo "The number of services has been increased"
    ;;
down) 
    if [ $COUNT -gt 5 ]
    then
        let "RESULT = $COUNT - 5"
    else
        RESULT=1
    fi
    docker compose up --scale backend=$RESULT -d
    echo "The number of services has been reduced"
    ;;
*) echo "Invalid option"
   ;;
esac