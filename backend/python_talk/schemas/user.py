# @Filename: user.py
# @Author: codists
# @Created: 2025-07-15 22:49:01
from marshmallow import fields, validate

from python_talk.schemas.base import BaseSchema


class UserSchema(BaseSchema):
    username = fields.Str(required=True, metadata={'description': '用户名'})
    password = fields.Str(required=True, metadata={'description': '密码'})
    email = fields.String(metadata={'description': '邮箱'})


