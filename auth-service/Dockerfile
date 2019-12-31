FROM python:3.7.3-alpine

RUN apk add --update mariadb-dev gcc libc-dev libffi-dev

COPY requirements.txt /usr/src/client/
RUN pip install --no-cache-dir -r /usr/src/client/requirements.txt

COPY app /usr/src/client/app
COPY start.py /usr/src/client/

EXPOSE 8888

CMD ["python", "/usr/src/client/start.py"]
