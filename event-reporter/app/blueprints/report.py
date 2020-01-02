from flask import Blueprint, redirect, render_template, url_for, request, flash
from werkzeug.datastructures import CombinedMultiDict

from app.extensions import MongoDatabase
from app.models import AlertCode, Event
from app.forms import ReportForm

blueprint = Blueprint("report", __name__, url_prefix='/report')


@blueprint.route("/", methods=['get'])
def report_event():
    form = ReportForm()
    return render_template('event/report.html', form=form)


@blueprint.route("/", methods=['post'])
def report_event_post():
    form = ReportForm(CombinedMultiDict((request.files, request.form)))

    if form.validate():
        image_extension = form.image.data.filename.split('.')[-1] if form.image.data else None

        ev = Event(
            timestamp=str(form.timestamp.data),
            latitude=form.latitude.data,
            longitude=form.longitude.data,
            alert_code=AlertCode.from_name(form.type.data),
            description=form.description.data,
            image_extension=image_extension
        )

        MongoDatabase.insert_event(ev)
        if ev.has_image():
            MongoDatabase.insert_photo(ev.get_image_name(), form.image.data)

        flash('Event reported')
        return redirect(url_for('event.show_events'))
    return render_template('event/report.html', form=form)
