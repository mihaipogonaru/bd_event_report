import os


class MailConfig:
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'pogonarumihai@gmail.com'
    MAIL_PASSWORD = 'wnnvfsolsmjecnry'
    MAIL_DEFAULT_SENDER = 'pogonarumihai@gmail.com'


class MongoConfig:
    MONGO_URL = 'mongo-db'
    MONGO_PORT = '27017'
    MONGO_DATABASE = 'EventReporter'
    MONGO_URI = "mongodb://{}:{}/{}".format(MONGO_URL, MONGO_PORT, MONGO_DATABASE)


class Config(MongoConfig, MailConfig):
    SECRET_KEY = "BD_SUPER_!@#SA$W!@%^%$df12^5#s9d8%09@#SxC%*_SECRET_KEY"
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    ADMIN_EMAILS = ['andistroie@gmail.com', 'pogonarumihai@gmail.com', 'andreidanielsafta@yahoo.com', 'madalina.mchirita@gmail.com']
    ASSETS_DEBUG = False


class ServerConfig:
    host = '0.0.0.0'
    port = 8888
    threaded = True
    debug = True
