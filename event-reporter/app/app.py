from flask import Flask, render_template, redirect, url_for

from app.config import Config
from app.assets import register_assets
from app.extensions import (
    db,
    login_manager
)
from app.blueprints import manage_bp, rapports_bp

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
    app.register_blueprint(manage_bp)
    app.register_blueprint(rapports_bp)


def register_extensions(app):
    db.set_session_read_commited()
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
    return redirect(url_for('manage.manage_index'))
