from datetime import datetime

from flask import Blueprint

from python_talk.models import User
from python_talk.utils.serializer import serializer
from python_talk.tasks import hello_world, async_send_email
from python_talk.utils.reqparse import RequestParser, LengthValidator, EmailValidator

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


@user_bp.post('/register')
def register():
    parser = RequestParser()
    parser.add_arg('email', validators=[EmailValidator()], required=True)
    parser.add_arg('username', validators=[LengthValidator(6, 15)], required=True)
    parser.add_arg('password', validators=[LengthValidator(1, 20)], required=True)
    arguments = parser.parse_args()

    if User.find_by_email(arguments.email):
        return {'code': 40001, 'message': '邮箱已存在'}, 400

    if User.find_by_username(arguments.username):
        return {'code': 40002, 'message': '用户名已存在'}, 400

    user = User(username=arguments.username, email=arguments.email, password=arguments.password)
    user.save()

    return {'code': 200, 'message': 'register success', 'data': serializer(user)}
