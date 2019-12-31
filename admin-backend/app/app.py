from flask import Flask, jsonify

from app.config import Config
from app.extensions import (
    db
)
from app.blueprints import city_bp, county_bp, user_bp

def create_app(config_object=Config):
    """An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_blueprints(app)
    register_error_handlers(app)

    return app

def register_blueprints(app):
    app.register_blueprint(city_bp)
    app.register_blueprint(county_bp)
    app.register_blueprint(user_bp)

def register_error_handlers(app):
    def render_error(error):
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)

        resp = {"status": "error", "error": str(error), "error_code": error_code}

        return jsonify(resp)
    for errcode in [401, 404, 500]:
        app.errorhandler(render_error)

app = create_app()
