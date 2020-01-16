#!/bin/bash

set -x
set -e

docker build --tag mpogonaru/bd_event-reporter_auth-db:latest auth-db/
docker build --tag mpogonaru/bd_event-reporter_auth-service:latest auth-service/
docker build --tag mpogonaru/bd_event-reporter_mongo:latest mongo-db/
docker build --tag mpogonaru/bd_event-reporter_app:latest event-reporter/
docker build --tag mpogonaru/bd_event-reporter_nginx:latest nginx/
