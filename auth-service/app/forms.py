import datetime as dt

from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms.fields.html5 import DateField

from app.messages import ValidationMessages, LoginValidationMessages
from app.extensions import db
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username (your e-mail)',
                           validators=[DataRequired(LoginValidationMessages.data_required),
                                       Email(LoginValidationMessages.email_format)])
    password = PasswordField('Password')
    remember = BooleanField('Keep me signed in')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False

        self.user = db.call_no_throw(db.select_user, email=self.username.data)

        if not self.user or self.user == db.err:
            self.password.errors.append('Invalid username or password')
            return False

        self.user = User(self.user)

        if not self.user.check_password(self.password.data):
            self.password.errors.append('Invalid username or password')
            return False

        return True


class RegisterForm(FlaskForm):
    username = StringField('Username (user e-mail)',
                           validators=[DataRequired(LoginValidationMessages.data_required),
                                       Email(LoginValidationMessages.email_format)])
    password = PasswordField('Password',
                             validators=[DataRequired(LoginValidationMessages.data_required)])

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.result = None

    def validate(self):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False

        try:
            db.insert_user(self.username.data, self.password.data)
        except Exception as e:
            self.username.errors.append(str(e))
            return False

        return True
