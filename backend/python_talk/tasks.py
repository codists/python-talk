"""
flask 是生产者，task是消费者
"""
from flask_mail import Message

from exts import mail, celery


@celery.task
def async_send_email(msg):
    msg = Message(msg)
    mail.send(msg)
