#!/bin/bash

docker volume rm idp_evp_db-data
docker network rm idp_evp_default idp_evp_frontend idp_evp_admin
