#!/bin/sh
docker run --name diffcalculator -t -d diffcalculator
p1="tmp/p1"
p2="tmp/p2"
docker exec diffcalculator pwd
docker cp $1 diffcalculator:$p1
docker cp $2 diffcalculator:$p2
docker exec diffcalculator python ./main.py -p1 $p1 -p2 $p2 -v
docker rm diffcalculator --force