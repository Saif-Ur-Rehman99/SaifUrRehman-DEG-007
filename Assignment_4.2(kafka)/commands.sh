#!/bin/bash

docker exec broker kafka-topics --create --topic topica --partitions 4 --replication-factor 1 --bootstrap-server broker:9092
docker exec broker kafka-topics --list --bootstrap-server broker:9092

