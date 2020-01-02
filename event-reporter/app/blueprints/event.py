from flask import Blueprint, render_template

from app.extensions import MongoDatabase

blueprint = Blueprint("event", __name__, url_prefix='/event')


@blueprint.route("/", methods=['get'])
def show_events():
    events = MongoDatabase.get_events()
    return render_template('event/map.html', events=events)


@blueprint.route("/<string:event>/", methods=['get'])
def show_event(event: str):
    ev = MongoDatabase.select_event(event)
    if not ev:
        return "", 404

    return render_template('event/event.html', ev=ev)


@blueprint.route("/image/<string:event>/", methods=['get'])
def get_event_image(event: str):
    with open("plm.jpg", 'w') as f:
        f.write(MongoDatabase.select_photo(event).read())

    return MongoDatabase.send_photo(event)
