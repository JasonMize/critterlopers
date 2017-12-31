#!/bin/sh

DIR=$(pwd)
echo $DIR

mkdir -p $DIR/docker-logs

docker kill critterlopers
docker rm critterlopers
docker run -v $DIR/docker-logs:/var/log/uwsgi -d -p 8088:80 --name critterlopers jason/critter:test
docker ps
