"""
application factory参考： https://flask.palletsprojects.com/en/latest/patterns/appfactories/
"""
from flask import Flask

from python_talk.config import config_class_name


def create_app(config_name=None):
    app = Flask(__name__)

    app.config.from_object(config_class_name[config_name])

    return app
