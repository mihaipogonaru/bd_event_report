import os


class Config:
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    ASSETS_DEBUG = False


class ServerConfig:
    host = '0.0.0.0'
    port = 9901
    threaded = True


class DBConfig:
    db_credentials_file = os.path.join(os.path.dirname(__file__), 'db_credentials')
    db_server = 'auth-db'
    db_user = open(db_credentials_file, 'r').readline().split(' ')[0].strip()
    db_password = open(db_credentials_file, 'r').readline().split(' ')[1].strip()
    db_port = 3306
    db_name = 'event_reporter'
    db_url = 'mysql://{}:{}@{}:{}/{}'.\
        format(db_user, db_password, db_server, db_port, db_name)
