from flask import Blueprint, redirect, render_template, url_for, request, flash

from app.extensions import MongoDatabase
from app.forms import ApproveForm
from app.utils import admin_required

blueprint = Blueprint("admin", __name__, url_prefix='/admin')


@blueprint.route("/", methods=['get'])
@admin_required
def event_approve_get():
    events = MongoDatabase.get_events(get_invisible=True)
    forms = [ApproveForm(event=e.name) for e in events if not e.is_visible()]

    return render_template('admin/event.html', forms=forms)


@blueprint.route("/", methods=['post'])
@admin_required
def event_approve_post():
    form = ApproveForm(request.form)
    name = str(form.name.data)

    if request.form['action'] == 'approve':
        MongoDatabase.update_event_display(name)
        flash("Event approved")
    elif request.form['action'] == 'delete':
        MongoDatabase.delete_event(name)
        flash("Event deleted")

    return redirect(url_for('admin.event_approve_get'))
