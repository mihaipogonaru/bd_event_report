from datetime import datetime

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import FloatField, TextAreaField, SelectField, DateTimeField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField

from app.extensions import MongoDatabase as db
from app.messages import ValidationMessages
from app.models import AlertCode


class ReportForm(FlaskForm):
    timestamp = DateTimeField('Date',
                              format='%d-%m-%Y %H:%M:%S',
                              default=datetime.now,
                              validators=[DataRequired(ValidationMessages.data_required)])
    latitude = FloatField('Latitude', validators=[DataRequired(ValidationMessages.data_required)])
    longitude = FloatField('Longitude', validators=[DataRequired(ValidationMessages.data_required)])
    type = SelectField('Type',
                       choices=[(ac.name, ac.name.lower()) for ac in AlertCode],
                       validators=[DataRequired(ValidationMessages.data_required)])
    description = TextAreaField('Description', validators=[DataRequired(ValidationMessages.data_required)])
    image = FileField('Image (.jpg .jpeg .png)',
                      validators=[FileAllowed(['jpg', 'jpeg', 'png'], ValidationMessages.file_extension)])

    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)

    def validate(self):
        initial_validation = super(ReportForm, self).validate()
        if not initial_validation:
            return False

        return True
