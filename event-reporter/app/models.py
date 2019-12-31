from flask_login import UserMixin

from app.messages import FatalErrorMessages


class User(UserMixin):
    def __init__(self, name):
        if name is None:
            print("----------------NO USER FOUND--------------------")
            raise Exception(FatalErrorMessages.no_user)

        self.id = name
