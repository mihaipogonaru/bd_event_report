from flask_mail import Mail, Message
from flask import render_template


class EvrMail:
    mail = Mail()

    @staticmethod
    def create_message(recipients, event):
        msg = Message(subject='New event reported: {}'.format(event.name),
                      recipients=recipients,
                      html=render_template('mail/new_event.html', ev=event))
        return msg

    @staticmethod
    def send_message(msg):
        EvrMail.mail.send(msg)
