from flask import render_template
from flask_mail import Mail, Message

from .database import MongoDatabase


class EvrMail:
    mail = Mail()

    @staticmethod
    def create_new_event_message(recipients, event):
        msg = Message(subject='New event reported: {}'.format(event.get_name_formatted()),
                      recipients=recipients)

        msg.html = render_template('mail/new_event.html', ev=event)
        if event.has_image():
            img = MongoDatabase.select_photo(event.get_image_name())

            if img:
                msg.attach(event.get_image_name(), 'image/{}'.format(event.image_extension),
                           img.read(), 'inline',
                           headers=({'Content-ID', '<{}>'.format(event.get_image_name())}, ))

        return msg

    @staticmethod
    def send_message(msg):
        EvrMail.mail.send(msg)
