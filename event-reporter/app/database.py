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
        evs = MongoDatabase.mongodb.db.events.find()
        events = [Event.from_document(ev) for ev in evs]

        return events

    @staticmethod
    def insert_event(event: Event):
        event_collection = MongoDatabase.mongodb.db.events
        event_collection.insert(event.to_document())

    @staticmethod
    def select_event(name: str):
        event_collection = MongoDatabase.mongodb.db.events
        event = event_collection.find_one({'name': name})

        return Event.from_document(event) if event else None

    @staticmethod
    def delete_event(name: str):
        event_collection = MongoDatabase.mongodb.db.events
        event_collection.delete_one({'name': name})

    @staticmethod
    def insert_photo(photo_data, file_name):
        MongoDatabase.mongodb.save_file(file_name, photo_data)

    @staticmethod
    def select_photo(file_name):
        fs = GridFS(MongoDatabase.mongodb.db)
        photo_data = fs.get_last_version(filename=file_name)

        return photo_data if photo_data else None

    @staticmethod
    def send_photo(file_name):
        return MongoDatabase.mongodb.send_file(file_name)

    # @staticmethod
    # def delete_photo(file_name):
    #    fs = GridFS(MongoDatabase.mongodb.db)
