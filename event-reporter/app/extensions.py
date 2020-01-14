"""Extensions module. Each extension is initialized in the app factory located
in app.py
"""

from .database import MongoDatabase
from .mail import EvrMail
from flask_login import LoginManager

login_manager = LoginManager()
