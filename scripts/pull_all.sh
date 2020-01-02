#!/bin/bash

set -x
set -e

docker pull mpogonaru/bd_event-reporter_auth-db:latest
docker pull mpogonaru/bd_event-reporter_auth-service:latest
docker pull mpogonaru/bd_event-reporter_mongo:latest
docker pull mpogonaru/bd_event-reporter_app:latest
docker pull mpogonaru/bd_event-reporter_nginx:latest
