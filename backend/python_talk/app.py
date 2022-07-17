"""
application factory reference： https://flask.palletsprojects.com/en/latest/patterns/appfactories/
"""
from flask import Flask

from python_talk.models import User
from python_talk.blueprints.user import user_bp
from python_talk.config import config_class_name
from python_talk.extensions import mail, celery, db, migrate


def create_app(config_name=None):
    """
    1.add config
    2.register extensions
    """
    app = Flask(__name__)
    app.config.from_object(config_class_name[config_name])
    register_extensions(app)
    register_blueprints(app)
    register_errorhandler(app)
    inject_shell(app)

    return app


def register_extensions(app):
    mail.init_app(app)
    celery.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    app.register_blueprint(user_bp, url_prefix='/user')


def inject_shell(app):

    @app.shell_context_processor
    def inject():
        return {
            'db': db,
            'User': User,
        }


def register_errorhandler(app):
    pass
