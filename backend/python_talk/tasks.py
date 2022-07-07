"""
flask 是生产者，task是消费者
"""
from exts import mail
from flask_mail import Message
from app import app

@celery_app.task
def async_send_email(msg):
    msg = Message(msg)
    mail.send(msg)
