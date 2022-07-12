"""
application factory reference： https://flask.palletsprojects.com/en/latest/patterns/appfactories/
"""
from flask import Flask

from python_talk.config import config_class_name
from python_talk.extensions import mail, celery, db


def create_app(config_name=None):
    """
    1.add config
    2.register extensions
    """
    app = Flask(__name__)
    app.config.from_object(config_class_name[config_name])
    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    mail.init_app(app)
    celery.init_app(app)
    db.init_app(app)


def register_blueprints(app):
    from python_talk.blueprints.user import user_bp

    app.register_blueprint(user_bp, url_prefix='/user')
