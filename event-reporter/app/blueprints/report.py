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
        ev = Event(
            timestamp=str(form.timestamp.data),
            latitude=form.latitude.data,
            longitude=form.longitude.data,
            alert_code=AlertCode.from_name(form.type.data),
            description=form.description.data
        )

        with open("always.txt", 'w') as f:
            f.write("HEY")

        MongoDatabase.insert_event(ev)
        if form.image.data:
            image_data = form.image.data

            with open("plm1.txt", 'w') as f:
                f.write("HEY")
                f.write(str(form.image.data.read()))

            MongoDatabase.insert_photo(ev.name, image_data)

        flash('Event reported')
        return redirect(url_for('event.show_events'))
    return render_template('event/report.html', form=form)
