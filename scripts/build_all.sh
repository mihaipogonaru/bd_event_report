#!/bin/bash

set -x
set -e

docker build --tag mpogonaru/bd_event-reporter_auth-db:latest auth-db/
docker push mpogonaru/bd_event-reporter_auth-db:latest

docker build --tag mpogonaru/bd_event-reporter_auth-service:latest auth-service/
docker push mpogonaru/bd_event-reporter_auth-service:latest

docker build --tag mpogonaru/bd_event-reporter_mongo:latest mongo-db/
docker push mpogonaru/bd_event-reporter_mongo:latest

docker build --tag mpogonaru/bd_event-reporter_app:latest event-reporter/
docker push mpogonaru/bd_event-reporter_app:latest

docker build --tag mpogonaru/bd_event-reporter_nginx:latest nginx/
docker push mpogonaru/bd_event-reporter_nginx:latest
