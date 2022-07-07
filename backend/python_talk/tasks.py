"""
flask 是生产者，task是消费者
"""
from flask_mail import Message

from exts import mail
from celery_app import make_celery
from app import app

cel = make_celery(app)


@cel.task
def async_send_email(msg):
    msg = Message(msg)
    mail.send(msg)
