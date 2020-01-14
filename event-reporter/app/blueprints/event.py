from flask import Blueprint, render_template

from app.extensions import MongoDatabase

blueprint = Blueprint("event", __name__, url_prefix='/event')


@blueprint.route("/", methods=['get'])
def show_events():
    events = MongoDatabase.get_events(get_invisible=False)
    return render_template('event/map.html', events=events)


@blueprint.route("/<string:event>/", methods=['get'])
def show_event(event: str):
    ev = MongoDatabase.select_event(event)
    if not ev:
        return "", 404

    ev_doc = ev.to_document()

    ev_name = ev_doc['name']
    ev_timestamp = ev_doc['timestamp']
    ev_latitude = ev_doc['latitude']
    ev_longitude = ev_doc['longitude']
    ev_alert_code = ev_doc['alert_code']
    ev_description = ev_doc['description']
    ev_tag = ev_doc['tag']

    return render_template('event/event.html', ev=ev, name=ev_name, timestamp=ev_timestamp, lat=ev_latitude,
                           long=ev_longitude, al_code=ev_alert_code, desc=ev_description, tag=ev_tag)


@blueprint.route("/image/<string:event>/", methods=['get'])
def get_event_image(event: str):
    ev = MongoDatabase.select_event(event)
    if not ev or not ev.has_image():
        return "", 404

    return MongoDatabase.send_photo(ev.get_image_name())
