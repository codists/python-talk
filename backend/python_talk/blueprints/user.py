"""
register
login
"""
import re
from datetime import timedelta

from flask import Blueprint, request, jsonify, g
from sqlalchemy.sql import or_, and_
from werkzeug.security import check_password_hash
from flask_mail import Message

from models import User
from utils.restful import restful
from utils.schema import Schema, StringField
from utils.security import create_access_token, identify, login_required
from tasks import async_send_email

user_bp = Blueprint('user', __name__, url_prefix='/user')

username_re = re.compile(r'[a-zA-Z_]+\w{0,14}')
email_re = re.compile(r'^[a-zA-Z0-9_]{4,20}@(163|126|gmail|qq)\.com')


class RegisterRequest(Schema):
    username = StringField()
    email = StringField()
    password = StringField()
    avatar = StringField()


def validate_username(username):
    return bool(username_re.match(username))


def validate_email(email):
    return bool(email_re.match(email))


@user_bp.post('/register')
def register():
    user_schema = RegisterRequest(**request.json)
    user = User.query.filter(
        or_(User.username == user_schema.username, User.email == user_schema.email)
    ).first()

    if user:
        message = []
        if user.username == user_schema.username:
            message.append('username')
        if user.email == user_schema.email:
            message.append('email')

        return restful.error(','.join(message) + ' already exists')

    if not validate_username(user_schema.username):
        return restful.error('The username does not meet the requirements')

    if not validate_email(user_schema.email):
        return restful.error('The email does not meet the requirements！')

    if not user_schema.password:
        return restful.error('password cannot be empty')

    user = User(**user_schema.to_dict()).save()
    return restful.success('Registration succeeded', data={'user_id': user.id})


@user_bp.get('/exist')
def is_user_exist():
    type_ = request.args.get('type')
    data = request.args.get('data')

    if type_ not in {'username', 'email'}:
        return restful.error('The type must be username or email')

    return restful.success(data={'exist': bool(User.query.filter_by(**{type_: data}).first())})


@user_bp.post('/login')
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username:
        return jsonify({'msg': '请填写用户名'}), 400
    if not password:
        return jsonify({'msg': '请填写密码'}), 400

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token, refresh_token = create_access_token(username, expires_delta=timedelta(minutes=2),
                                                          need_refresh_token=True)
        return jsonify({'success': True, 'access_token': access_token, 'refresh_token': refresh_token}), 200
    else:
        return jsonify({'success': False, 'message': '用户名或者密码错误'}), 401


@user_bp.post('/current_user')
@login_required
def current_user():
    """
    get current user info.
    :return: json
    """
    if g.user_id:
        return jsonify({'success': True, 'msg': 'ok'}), 200
    return jsonify({'success': False, 'token': 'Permission Denied'}), 403


@user_bp.post('/token')
def update_access_token():
    """
    1.通过refresh_token获取新的access_token
    2.请求该函数的时候，使用的是refresh_token
    """
    if g.user_id and g.is_refresh:
        access_token, _ = create_access_token(g.user_id)
        return jsonify({'success': True, 'access_token': access_token, 'msg': '更新access_token成功'}), 201
    else:
        return jsonify({'success': False, 'msg': 'refresh_token错误'}), 403


@user_bp.post('/mail')
def register_verify():
    msg = Message('Hello from Flask', recipients=['952328342@qq.com'])
    msg.body = 'This is a test email sent from a background Celery task.'
    async_send_email.delay(msg)
