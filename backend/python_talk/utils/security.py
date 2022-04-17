"""
jwt authorization：
ref1：https://blog.51cto.com/u_15081058/2595182
ref2: https://github.com/yaoyonstudio/flask-pyjwt-auth
"""
# 采用secrets库随机生成SECRET_KEY
from datetime import timedelta, datetime

import jwt

from ..config import SECRET_KEY, ALGORITHM


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
        'iat':  datetime.datetime.utcnow(),

        # 自定义字段
        'data': {
            'id': username,
        },
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
        return '无效Token'
    else:
        return payload


def identify(auth_header: str):
    """
    用户鉴权：验证payload里面的信息和设置的是否一样
    """
    # TODO complete before 2022-04-18.





