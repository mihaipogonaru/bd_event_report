FROM python:3.7.3-alpine

RUN apk add --update mariadb-dev gcc libc-dev libffi-dev

COPY requirements.txt /usr/src/admin-backend/
RUN pip install --no-cache-dir -r /usr/src/admin-backend/requirements.txt

COPY insert_test_counties.py /usr/src/admin-backend/
COPY insert_test_data.py /usr/src/admin-backend/

COPY app /usr/src/admin-backend/app
COPY start.py /usr/src/admin-backend/

EXPOSE 9901
CMD python /usr/src/admin-backend/insert_test_counties.py\
  && python /usr/src/admin-backend/insert_test_data.py\
  && python /usr/src/admin-backend/start.py
