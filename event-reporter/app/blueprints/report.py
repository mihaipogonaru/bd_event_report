from flask import Blueprint, redirect, render_template, url_for, request, flash
from werkzeug import secure_filename

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
    form = ReportForm(request.form)

    if form.validate():
        ev = Event(
            timestamp=str(form.timestamp.data),
            latitude=str(form.latitude.data),
            longitude=str(form.longitude.data),
            alert_code=AlertCode.from_name(form.type.data),
            description=form.description.data
        )

        MongoDatabase.insert_event(ev)
        if form.image.data:
            MongoDatabase.insert_photo(form.image.data, ev.name)

        flash('Event reported')
        return redirect(url_for('event.show_events'))
    return render_template('event/report.html', form=form)
