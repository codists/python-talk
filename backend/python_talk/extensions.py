from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_smorest import Api

# from python_talk.celery_app import Celery

mail = Mail()
# celery = Celery()
db = SQLAlchemy()
migrate = Migrate()
api = Api()
