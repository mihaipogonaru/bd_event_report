from flask import Blueprint, render_template

from app.extensions import MongoDatabase
from app.models import Event

blueprint = Blueprint("event", __name__, url_prefix='/event')


@blueprint.route("/", methods=['get'])
def show_events():
    # list of dictionaries
    evs = MongoDatabase.call_no_throw(MongoDatabase.get_events)
    events = []

    if evs != MongoDatabase.err:
        events = [Event(e['timestamp'], e['latitude'], e['longitude'], e['alert_code'], e['description'],
                        e['photo_name'], e['tag']).to_dict() for e in evs]

    return render_template('event/map.html', events=events)
