from flask import Flask, render_template, redirect, url_for

from app.config import Config
from app.assets import register_assets
from app.extensions import (
    MongoDatabase,
    login_manager
)
from app.blueprints import event_bp, report_bp, admin_bp

from app.models import User, AlertCode, Event


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
    app.register_blueprint(event_bp)
    app.register_blueprint(report_bp)
    app.register_blueprint(admin_bp)


def register_extensions(app):
    MongoDatabase.mongodb.init_app(app)
    login_manager.init_app(app)


def register_error_handlers(app):
    def render_error(error):
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template("http_error/{0}.html".format(error_code)), error_code
    for errcode in [401, 500]:
        app.errorhandler(errcode)(render_error)


app = create_app()


@login_manager.user_loader
def load_user(user_email):
    return User(user_email)


#@login_manager.request_loader
#def load_user_from_request(request):
#    user_name = request.headers.get('Remote-User')
#
#    return User(user_name)


@app.route("/", methods=['get'])
def home():
    return redirect(url_for('event.show_events'))
