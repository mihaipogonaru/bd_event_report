#!/bin/bash

set -x
set -e

docker build --no-cache --tag mpogonaru/bd_event-reporter_auth-db:andi auth-db/
#docker push mpogonaru/bd_event-reporter_auth-db:latest

docker build --no-cache --tag mpogonaru/bd_event-reporter_auth-service:andi auth-service/
#docker push mpogonaru/bd_event-reporter_auth-service:latest

docker build --no-cache --tag mpogonaru/bd_event-reporter_mongo:andi mongo-db/
#docker push mpogonaru/bd_event-reporter_mongo:latest

docker build --no-cache --tag mpogonaru/bd_event-reporter_app:andi event-reporter/
#docker push mpogonaru/bd_event-reporter_app:latest

docker build --no-cache --tag mpogonaru/bd_event-reporter_nginx:andi nginx/
#docker push mpogonaru/bd_event-reporter_nginx:latest
