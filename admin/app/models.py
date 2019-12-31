from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_dict):
        if not user_dict:
            self.id = None
            self.email = None
            self.password = None
        else:
            self.email = user_dict['email']
            self.id = self.email
            self.password = user_dict['password']

    def check_password(self, value):
        return self.password == value
    