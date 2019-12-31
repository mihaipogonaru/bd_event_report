"""Extensions module. Each extension is initialized in the app factory located
in app.py
"""

from .database import Database as db
from flask_login import LoginManager

login_manager = LoginManager()
