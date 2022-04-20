"""
jwt authorization：
ref1：https://blog.51cto.com/u_15081058/2595182
ref2: https://github.com/yaoyonstudio/flask-pyjwt-auth
"""
# 采用secrets库随机生成SECRET_KEY
from datetime import timedelta, datetime
from functools import wraps

import jwt
from flask import request,jsonify

from config import SECRET_KEY, ALGORITHM


def create_access_token(username: str,  expires_delta: timedelta | None = None):
    """
    生成JWT
    """
    # 设置过期时间
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        # 默认过期时间为7天
        expire = datetime.utcnow() + timedelta(day=7)

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
        'username': username,
        # 标识是否为一次性token，1是，0不是。
        'flag': 1,
    }

    # 生成token
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def parse_access_token(auth_token: str):
    """
    解析token:
    """
    try:
        payload = jwt.decode(auth_token, SECRET_KEY, ALGORITHM)
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, jwt.InvalidSignatureError):
        return None
    else:
        return payload


def identify(auth_token: str):
    """
    用户鉴权：验证payload里面的信息和设置的是否一样
    """
    if auth_token:
        payload = parse_access_token(auth_token)
        if payload:
            if 'username' in payload and 'flag' in payload:
                if payload['flag'] == 0:
                    return payload['username']
                else:
                    return False
        else:
            return False
    return False


def login_required(func):
    """
    验证用户是否登录
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_token = request.headers.get('Authorization', None)
        if not auth_token:
            return jsonify({'success': False, 'message': 'Permission Denied'}), 403
        username = identify(auth_token)
        if username:
            return func(*args, **kwargs)
        return jsonify({'success': False, 'message': 'Permission Denied'}), 403
    return wrapper



