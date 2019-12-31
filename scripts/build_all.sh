#!/bin/bash

set -x
set -e

docker build --tag mpogonaru/admin:local admin/
docker build --tag mpogonaru/admin-backend:local admin-backend/

docker build --tag mpogonaru/bd_event-reporter_auth-db:v0.1 auth-db/
docker push mpogonaru/bd_event-reporter_auth-db:v0.1

docker build --tag mpogonaru/bd_event-reporter_auth-service:v0.1 auth-service/
docker push mpogonaru/bd_event-reporter_auth-service:v0.1

docker build --tag mpogonaru/bd_event-reporter_mongo:v0.1 mongo-db/
docker push mpogonaru/bd_event-reporter_mongo:v0.1

docker build --tag mpogonaru/bd_event-reporter_app:v0.1 event-reporter/
docker push mpogonaru/bd_event-reporter_app:v0.1

docker build --tag mpogonaru/bd_event-reporter_nginx:v0.1 nginx/
docker push mpogonaru/bd_event-reporter_nginx:v0.1
