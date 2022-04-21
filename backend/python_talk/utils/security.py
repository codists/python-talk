"""
jwt authorization：
ref1：https://blog.51cto.com/u_15081058/2595182
ref2: https://github.com/yaoyonstudio/flask-pyjwt-auth
"""
# 采用secrets库随机生成SECRET_KEY
from datetime import timedelta, datetime
from functools import wraps

import jwt
from flask import request, jsonify, g

from config import SECRET_KEY, ALGORITHM


def create_access_token(user_id: str,  expires_delta: timedelta | None = None):
    """
    生成JWT
    """
    # 设置过期时间
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        # 默认过期时间为7天
        expire = datetime.utcnow() + timedelta(days=7)
    # 设置payload
    payload = {
        # JWT规定了七个官方字段：https://datatracker.ietf.org/doc/html/rfc7519#section-4.1
        # 过期时间
        'exp': expire,
        # 签发人
        'iss': 'python-talk',
        # 签发时间
        'iat':  datetime.utcnow(),

        # 自定义字段
        'user_id': user_id,
        # 标识是否为一次性token，1是，0不是。
        'flag': 1,
    }

    # 生成token
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def parse_access_token(auth_token: str):
    """
    解析token:
    JWT所有的异常都继承自 PyJWTError
    """
    try:
        payload = jwt.decode(auth_token, SECRET_KEY, algorithms='HS256')
    except jwt.ExpiredSignatureError:
        return None
    return payload


def identify():
    """
    用户鉴权：验证payload里面的信息和设置的是否一样
    """

    g.user_id = None
    auth_header = request.headers.get('Authorization')
    if auth_header:
        # the format of JWT in frontend:Authorization: Bearer <token>,参考： https://jwt.io/introduction/
        auth_token = auth_header.split(' ')
        if auth_token and auth_token[0] == 'Bearer' and len(auth_token) == 2:
            payload = parse_access_token(auth_token[1])
            if payload:
                g.user_id = payload.get('user_id')


def login_required(func):
    """
    authorization.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        identify()
        if not g.user_id:
            return jsonify({'success': False, 'message': 'Permission Denied'}), 403
        else:
            return func(*args, **kwargs)
    return wrapper



