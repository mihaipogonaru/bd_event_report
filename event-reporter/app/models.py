from flask_login import UserMixin

from app.messages import FatalErrorMessages


class User(UserMixin):
    def __init__(self, name):
        if name is None:
            raise Exception(FatalErrorMessages.no_user)

        self.id = name


class Event:
    def __init__(self, timestamp, latitude, longitude, alert_code, description, photo_name, tag):
        self.timestamp = timestamp
        self.latitude = latitude
        self.longitude = longitude
        self.alert_code = alert_code
        self.description = description
        self.photo_name = photo_name
        self.tag = tag

    def to_dict(self):
        dictionary = {
            'timestamp': self.timestamp,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'alert_code': self.alert_code,
            'description': self.description,
            'photo_name': self.photo_name,
            'tag': self.tag
        }
        # return self.__dict__
        return dictionary
