from flask import Blueprint, render_template, request, redirect, url_for, flash

from app.admin_backend import AdminBackend
from app.forms import AddUser, ViewUser, RemoveUser

blueprint = Blueprint("user", __name__, url_prefix='/user')

@blueprint.route("/add/", methods=['get'])
def add():
    form = AddUser()
    return render_template('user/add.html', form=form)

@blueprint.route("/add/", methods=['post'])
def add_post():
    form = AddUser(request.form)

    if form.validate_on_submit():
        flash('Added successfully')
        return redirect(url_for('user.viewall'))

    return render_template('user/add.html', form=form)

@blueprint.route("/viewall/", methods=['get'])
def viewall():
    users_details = AdminBackend.view_users()

    if "error" in users_details:
        flash(users_details['error'])
        return render_template('user/viewall.html', users={})

    if not isinstance(users_details, list):
        users_details = [users_details]

    return render_template('user/viewall.html', users=users_details)

@blueprint.route("/remove/", methods=['get'])
def remove():
    form = RemoveUser()
    return render_template('user/remove.html', form=form)

@blueprint.route("/remove/", methods=['post'])
def remove_post():
    form = RemoveUser(request.form)

    if form.validate_on_submit():
        flash('Removed successfully')
        return redirect(url_for('user.viewall'))

    return render_template('user/remove.html', form=form)
