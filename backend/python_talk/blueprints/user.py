from datetime import datetime

from flask import Blueprint
from python_talk.tasks import hello_world, async_send_email

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.get('/')
def test():
    print('test')
    hello_world.delay()
    return 'This is test'


@user_bp.get('/email')
def send_email():
    async_send_email.delay()
    return f'{datetime.now()}Email had been sent'
