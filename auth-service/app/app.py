from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user

from app.config import Config
from app.assets import register_assets
from app.extensions import (
    db,
    login_manager
)

from app.models import User

from app.forms import LoginForm, RegisterForm
from app.utils import logout_required


def create_app(config_object=Config):
    """An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_blueprints(app)
    register_error_handlers(app)

    register_extensions(app)
    register_assets(app)

    return app


def register_blueprints(app):
    pass


def register_extensions(app):
    login_manager.init_app(app)


def register_error_handlers(app):
    pass


@login_manager.user_loader
def load_user(user_email):
    user = db.call_no_throw(db.select_user, email=user_email)
    if user == db.err or not user:
        return None

    return User(user)


app = create_app()


@app.route("/", methods=['get'])
@login_required
def auth():
    return "", 200


@app.route("/login/", methods=['get'])
@logout_required
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)


@app.route("/login/", methods=['post'])
@logout_required
def login_post():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        login_user(form.user, remember=form.remember.data)
        return redirect('/')

    return render_template('auth/login.html', form=form)


@app.route("/register/", methods=['get'])
def register():
    form = RegisterForm()
    return render_template('auth/register.html', form=form)


@app.route("/register/", methods=['post'])
def register_post():
    form = RegisterForm(request.form)

    if form.validate_on_submit():
        return redirect(url_for('login'))

    return render_template('auth/register.html', form=form)


@app.route("/logout/")
@login_required
def logout():
    logout_user()
    flash('You are logged out.', 'info')
    return redirect('/')
