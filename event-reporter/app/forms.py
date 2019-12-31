from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms.fields.html5 import DateField

from app.extensions import db


class BirthForm(FlaskForm):
    pin = IntegerField('Personal identity number',
                       validators=[DataRequired()])
    surname = StringField('Surname',
                          validators=[DataRequired()])
    name = StringField('Name',
                       validators=[DataRequired()])
    city = StringField('City',
                       validators=[DataRequired()])
    dt = DateField('', format='%Y-%m-%d',
                   validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(BirthForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        initial_validation = super(BirthForm, self).validate()
        if not initial_validation:
            return False

        if db.call_no_throw(db.insert_birth, pin=self.pin.data,
                            surname=self.surname.data, name=self.name.data,
                            city=self.city.data, date=self.dt.data) == db.err:
            
            self.pin.errors.append('Invalid pin or city')
            self.city.errors.append('Invalid pin or city')
            return False

        return True


class DeathForm(FlaskForm):
    pin1 = IntegerField('Personal identity number',
                        validators=[DataRequired()])
    city1 = StringField('City',
                        validators=[DataRequired()])
    dt1 = DateField('', format='%Y-%m-%d',
                    validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(DeathForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        initial_validation = super(DeathForm, self).validate()
        if not initial_validation:
            return False

        if db.call_no_throw(db.insert_death, person=self.pin1.data,
                            city=self.city1.data, date=self.dt1.data) == db.err:
            
            self.pin1.errors.append('Invalid pin or city')
            self.city1.errors.append('Invalid pin or city')
            return False

        return True
