from flask import Flask, render_template, redirect, url_for

from app.config import Config
from app.assets import register_assets
from app.extensions import (
    login_manager
)
from app.blueprints import city_bp, county_bp, user_bp

from app.models import User

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
    app.register_blueprint(city_bp)
    app.register_blueprint(county_bp)
    app.register_blueprint(user_bp)


def register_extensions(app):
    login_manager.init_app(app)


def register_error_handlers(app):
    def render_error(error):
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template("http_error/{0}.html".format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)


@login_manager.user_loader
def load_user(user_email):
    user = User({})
    return user

app = create_app()


@app.route("/", methods=['get'])
def home():
    return redirect(url_for('user.viewall'))
