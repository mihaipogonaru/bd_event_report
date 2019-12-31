import os


class MongoConfig:
    MONGO_URL = 'mongo-db'
    MONGO_PORT = '27017'
    MONGO_URI = "mongodb://{}:{}/EventReporter".format(MONGO_URL, MONGO_PORT)


class Config(MongoConfig):
    SECRET_KEY = "BD_SUPER_!@#SA$W!@%^%$df12^5#s9d8%09@#SxC%*_SECRET_KEY"
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    ASSETS_DEBUG = False


class ServerConfig:
    host = '0.0.0.0'
    port = 8888
    threaded = True
    debug = True
