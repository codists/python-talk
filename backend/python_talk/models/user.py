# @Filename: user.py
# @Author: codists
# @Created: 2025-07-14 23:04:29

from python_talk.extensions import db
from python_talk.models.base import ModelMixin, PkModel


class User(PkModel, ModelMixin):
    __tablename__ = 'users'

    username = db.Column(db.String(128), index=True, unique=True, comment='用户名')
    password = db.Column(db.String(64), comment='密码')
    email = db.Column(db.String(128), index=True, unique=True, comment='邮箱')
