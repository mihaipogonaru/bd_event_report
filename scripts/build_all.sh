#!/bin/bash

set -x
set -e

docker build  --tag mpogonaru/bd_event-reporter_auth-db:sft auth-db/
#docker push mpogonaru/bd_event-reporter_auth-db:latest

docker build  --tag mpogonaru/bd_event-reporter_auth-service:sft auth-service/
#docker push mpogonaru/bd_event-reporter_auth-service:latest

docker build  --tag mpogonaru/bd_event-reporter_mongo:sft mongo-db/
#docker push mpogonaru/bd_event-reporter_mongo:latest

docker build  --tag mpogonaru/bd_event-reporter_app:sft event-reporter/
#docker push mpogonaru/bd_event-reporter_app:latest

docker build  --tag mpogonaru/bd_event-reporter_nginx:sft nginx/
#docker push mpogonaru/bd_event-reporter_nginx:latest
