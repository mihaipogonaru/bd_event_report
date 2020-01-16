#!/bin/bash

if [[ "$#" -ne 1 ]]; then
    echo "Uasge: $0 if-name"
    exit 1
fi

docker swarm init --advertise-addr $1
