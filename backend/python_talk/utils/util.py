from functools import wraps
from flask import request
from .security import identify


def login_required(func):
    """
    登录保护，验证用户是否登录
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization', default=None)
        if not token:
            return 'Not Login', '403 Permission Denied'

        username = identify(token)
        if not username:
            return 'not login', '403 Permission Denied'

        return func(*args, **kwargs)

    return wrapper()














