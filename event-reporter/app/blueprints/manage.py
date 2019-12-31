from flask import Blueprint, flash, render_template, request, redirect, url_for

from app.forms import BirthForm, DeathForm

from datetime import datetime

blueprint = Blueprint("manage", __name__, url_prefix='/manage')


@blueprint.route("/", methods=['get'])
def manage_index():
    form_b = BirthForm()
    form_d = DeathForm()
    return render_template('manage/index.html', form_b=form_b, form_d=form_d)


@blueprint.route("/birth", methods=['post'])
def manage_birth_post():
    form_b = BirthForm(request.form)
    form_d = DeathForm()

    if form_b.validate_on_submit():
        flash('Birth added')
        return redirect(url_for('manage.manage_index'))

    return render_template('manage/index.html', form_b=form_b, form_d=form_d)


@blueprint.route("/death", methods=['post'])
def manage_death_post():
    form_b = BirthForm()
    form_d = DeathForm(request.form)

    if form_d.validate_on_submit():
        flash('Death added')
        return redirect(url_for('manage.manage_index'))

    return render_template('manage/index.html', form_b=form_b, form_d=form_d)
