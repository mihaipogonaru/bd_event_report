from enum import Enum

from flask_login import UserMixin

from app.messages import FatalErrorMessages


class User(UserMixin):
    def __init__(self, name):
        if name is None:
            raise Exception(FatalErrorMessages.no_user)

        self.id = name


class AlertCode(Enum):
    FIRE = 1
    EXPLOSION = 2
    TORNADO = 3

    @staticmethod
    def from_code(code: str):
        return AlertCode(code)

    @staticmethod
    def from_name(name: str):
        return AlertCode[name]


class Event:
    def __init__(self, timestamp: str, latitude: float, longitude: float, alert_code: AlertCode, description: str,
                 image_extension: str, tag: str = None):
        self.timestamp = timestamp
        self.latitude = latitude
        self.longitude = longitude
        self.alert_code = alert_code
        self.description = description
        self.image_extension = image_extension
        self.tag = tag

        self.name = "{}_{}_{}_{}".format(alert_code.name, timestamp, latitude, longitude).replace(" ", "_")

    def has_image(self):
        return bool(self.image_extension)

    def get_image_name(self):
        if not self.has_image():
            return None

        return "{}.{}".format(self.name, self.image_extension)

    @staticmethod
    def from_document(e: dict):
        alert_code = AlertCode.from_name(e['alert_code'])

        return Event(
            timestamp=e['timestamp'],
            latitude=e['latitude'],
            longitude=e['longitude'],
            alert_code=alert_code,
            description=e['description'],
            image_extension=e['image_extension'],
            tag=e['tag']
        )

    def to_document(self):
        dictionary = {
            'name': self.name,
            'timestamp': self.timestamp,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'alert_code': self.alert_code.name,
            'description': self.description,
            'image_extension': self.image_extension,
            'tag': self.tag
        }
        # return self.__dict__
        return dictionary
