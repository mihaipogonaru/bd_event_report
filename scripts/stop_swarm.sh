#!/bin/bash

docker stack rm bd_evr
docker swarm leave --force
