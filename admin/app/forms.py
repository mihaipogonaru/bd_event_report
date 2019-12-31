import datetime as dt

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

from app.messages import ValidationMessages
from app.models import User
from app.admin_backend import AdminBackend

class AddUser(FlaskForm):
    username = StringField('Username (user e-mail)',
                           validators=[DataRequired(ValidationMessages.data_required),
                                       Email(ValidationMessages.email_format)])
    password = PasswordField('Password',
                           validators=[DataRequired(ValidationMessages.data_required)])

    def __init__(self, *args, **kwargs):
        super(AddUser, self).__init__(*args, **kwargs)
        self.result = None

    def validate(self):
        initial_validation = super(AddUser, self).validate()
        if not initial_validation:
            return False

        self.result = AdminBackend.add_user(self.username.data, self.password.data)

        if "error" in self.result:
            self.username.errors.append(self.result["error"])
            return False

        return True

class ViewUser(FlaskForm):
    username = StringField('Username (user e-mail)',
                           validators=[DataRequired(ValidationMessages.data_required),
                                       Email(ValidationMessages.email_format)])

    def __init__(self, *args, **kwargs):
        super(ViewUser, self).__init__(*args, **kwargs)
        self.user_details = None

    def validate(self):
        initial_validation = super(ViewUser, self).validate()
        if not initial_validation:
            return False

        self.user_details = AdminBackend.view_user(self.username.data)
        if "error" in self.user_details:
            self.username.errors.append(self.user_details["error"])
            return False

        return True

class RemoveUser(FlaskForm):
    username = StringField('Username (user e-mail)',
                           validators=[DataRequired(ValidationMessages.data_required),
                                       Email(ValidationMessages.email_format)])

    def __init__(self, *args, **kwargs):
        super(RemoveUser, self).__init__(*args, **kwargs)
        self.result = None

    def validate(self):
        initial_validation = super(RemoveUser, self).validate()
        if not initial_validation:
            return False

        self.result = AdminBackend.remove_user(self.username.data)

        if "error" in self.result:
            self.username.errors.append(self.result["error"])
            return False

        return True
