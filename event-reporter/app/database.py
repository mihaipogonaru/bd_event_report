from flask_pymongo import PyMongo
from gridfs import GridFS

from app.models import Event


class MongoDatabase:
    mongodb = PyMongo()
    err = 'err'

    @staticmethod
    def call_no_throw(method, *args, **kwargs):
        try:
            return method(*args, **kwargs)
        except:
            return MongoDatabase.err

    @staticmethod
    def get_events():
        events = MongoDatabase.mongodb.db.events.find()
        return events if events else None

    @staticmethod
    def insert_event(event: Event):
        event_collection = MongoDatabase.mongodb.db.events
        event_collection.insert(event.to_dict())

    @staticmethod
    def select_event(latitude, longitude, file_name):
        event_collection = MongoDatabase.mongodb.db.events
        event = event_collection.find({'latitude': latitude, 'longitude': longitude, 'file_name': file_name})
        return event if event else None

    @staticmethod
    def delete_event(latitude, longitude, file_name):
        event_collection = MongoDatabase.mongodb.db.events
        event_collection.delete_one({'latitude': latitude, 'longitude': longitude, 'file_name': file_name})

    @staticmethod
    def insert_photo(photo_data, file_name):
        fs = GridFS(MongoDatabase.mongodb.db)
        fs.put(photo_data, filename=file_name)

    @staticmethod
    def select_photo(file_name):
        fs = GridFS(MongoDatabase.mongodb.db)
        photo_data = fs.get_last_version(filename=file_name)
        return photo_data if photo_data else None

    # @staticmethod
    # def delete_photo(file_name):
    #    fs = GridFS(MongoDatabase.mongodb.db)
