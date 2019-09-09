#!/bin/sh

docker-compose up -d elasticsearch
sleep 10
docker-compose up -d searchapp
docker-compose run twint -u lucmichalski -es elasticsearch:9200 --json -o /opt/twint/lucmichalski.json
