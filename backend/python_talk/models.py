from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from exts import db


class Base(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<{self.__class__.__name__!r} {self.__dict__!r}>'


class User(Base):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    __password = db.Column('password', db.String(255), nullable=False)
    avatar = db.Column(db.String(512))

    def __init__(self, username, email, password, avatar=None):
        self.username = username
        self.email = email
        self.password = password
        self.avatar = avatar

    @property
    def password(self):
        raise AttributeError('password field is not allowed to access')

    @password.setter
    def password(self, value):
        self.__password = generate_password_hash(value)

    def check_password(self, value):
        return check_password_hash(self.__password, value)
