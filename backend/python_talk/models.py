"""
1.pep249: https://peps.python.org/pep-0249/
2.flask-sqlalchemy: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
"""
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from python_talk.extensions import db


class Base(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<{self.__class__.__name__!r} {self.__dict__!r}>'

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_by_id(cls, id_):
        return cls.query.get(id_)


class User(Base):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    __password = db.Column('password', db.String(255), nullable=False)
    avatar = db.Column(db.String(512))

    __serializer__ = ['id', 'username', 'email', 'avatar', 'created_at']

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

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
