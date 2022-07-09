from flask_mail import Mail

from python_talk.celery_app import Celery

mail = Mail()
celery = Celery()
