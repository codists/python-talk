"""
register
login
"""
import re

from flask import Blueprint, request, jsonify
from sqlalchemy.sql import or_

from models import User
from utils.restful import restful
from utils.schema import Schema, StringField
from utils.security import create_access_token

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
    username = request.json['username']
    password = request.json['password']

    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    user = User.get_or_none(User.username == username, User.password == password)

    if user is None:
        return jsonify({'success': False, 'message': 'Bad username or password'}), 401

    access_token = create_access_token(identity=username)
    return jsonify({'success': True, 'token': access_token}), 200

