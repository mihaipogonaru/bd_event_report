#!/bin/bash

set -x
set -e

docker push mpogonaru/bd_event-reporter_auth-db:latest
docker push mpogonaru/bd_event-reporter_auth-service:latest
docker push mpogonaru/bd_event-reporter_mongo:latest
docker push mpogonaru/bd_event-reporter_app:latest
docker push mpogonaru/bd_event-reporter_nginx:latest
