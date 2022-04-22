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


def create_access_token(user_id: str,  expires_delta: timedelta | None = None, need_refresh_token=False):
    """
    生成JWT
    :need_refresh_token: 当更新access_token的时候该参数的值为False
    """
    # 设置过期时间
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        # 默认过期时间为7天
        expire = datetime.utcnow() + timedelta(minutes=1)
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
        # 标识是否是refresh_token
        'is_refresh': False,
    }
    # 生成access_token
    access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    # 生成refresh_token
    refresh_token = None
    if need_refresh_token:
        payload.update({
            'exp':  datetime.utcnow() + timedelta(days=14),
            'is_refresh': True
        })
        refresh_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return access_token,  refresh_token


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
    鉴权,用于每次请求前获取token
    """
    g.user_id = None
    g.is_refresh = False
    auth_header = request.headers.get('Authorization')
    if auth_header:
        # the format of JWT in frontend:Authorization: Bearer <token>,参考： https://jwt.io/introduction/
        auth_token = auth_header.split(' ')
        if auth_token and auth_token[0] == 'Bearer' and len(auth_token) == 2:
            payload = parse_access_token(auth_token[1])
            if payload:
                g.user_id = payload.get('user_id')
                g.is_refresh = payload.get('is_refresh')


def login_required(func):
    """
    require login.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not g.user_id:
            return jsonify({'success': False, 'message': '未授权！'}), 401
        elif g.is_refresh:
            return jsonify({'success': False, 'message': '请使用access_token,不要使用refresh_token！'}), 403
        else:
            return func(*args, **kwargs)
    return wrapper






