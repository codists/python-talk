"""
application factory reference： https://flask.palletsprojects.com/en/latest/patterns/appfactories/
"""
from flask import Flask

from python_talk.blueprints.user import user_bp
from python_talk.extensions import api, db, mail, migrate
from python_talk.models import User
from python_talk.api import register_blueprint


def configure_app(app: Flask):
    """配置app

    """
    from python_talk import config
    config.load(app)
    app.url_map.strict_slashes = False

def create_app():
    """
    1.add config
    2.register extensions
    """
    app = Flask(__name__)
    configure_app(app)
    register_extensions(app)
    register_blueprint()
    register_errorhandler(app)
    inject_shell(app)

    return app


def register_extensions(app):
    mail.init_app(app)
    # celery.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)


def inject_shell(app):

    @app.shell_context_processor
    def inject():
        return {
            'db': db,
            'User': User,
        }


def register_errorhandler(app):
    pass
