from flask import Blueprint, redirect, render_template, url_for, request, flash

from app.extensions import MongoDatabase
from app.models import Event
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
        flash('Event reported')
        redirect(url_for('event.show_events'))

    return render_template('event/report.html', form=form)
