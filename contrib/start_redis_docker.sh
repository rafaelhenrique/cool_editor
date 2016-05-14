#!/bin/bash
PORT=6379
NAME=cool_editor
VOLUME=$(pwd)/data_redis
SO=$(uname)
REDIS_PASSWORD=123

if [ $SO == "Linux" ]; then
   sysctl -w vm.overcommit_memory=1
   sysctl -w net.core.somaxconn=65535
   echo never > /sys/kernel/mm/transparent_hugepage/enabled
fi

mkdir -p $VOLUME
docker pull redis
docker run -t -i -p $PORT:$PORT --name $NAME -v $VOLUME:/data redis redis-server --appendonly yes --requirepass $REDIS_PASSWORD
if [ $? -ne 0 ]; then
   docker start $NAME
   CONTAINER_ID=$(docker ps -a -f name=$NAME --format "{{.ID}}")
   docker logs -f $CONTAINER_ID
fi
