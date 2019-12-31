import os


class Config:
    SECRET_KEY = "IDP_SUPER_!@#SA$W!@%^%$df12^5#s9d8%09@#SxC%*_SECRET_KEY"
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    ASSETS_DEBUG = False


class ServerConfig:
    host = '0.0.0.0'
    port = 9900
    threaded = True
