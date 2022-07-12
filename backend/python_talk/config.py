"""
1.flask configuration reference：https://flask.palletsprojects.com/en/latest/config/
2.from_object() reference：https://flask.palletsprojects.com/en/latest/config/#development-production
"""
import os
import sys

# root directory
basedir = os.path.abspath(os.path.dirname(__file__))

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class Config(object):
    TESTING = False

    # email
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465  # gmail: 587, qq mail:465, 163 mail: 465/994(ssl), 25(non-ssl)
    MAIL_USERNAME = 'codists@163.com'
    MAIL_PASSWORD = 'IYUUWQLLOBSVBRWL'
    MAIL_DEFAULT_SENDER = 'codists@163.com'
    MAIL_USE_SSL = True
    # MAIL_USE_TLS = False

    # celery
    CELERY_CONFIG = {
        'broker_url': 'redis://localhost:6379/0',
        'result_backend': 'redis://localhost:6379/0'
    }

    # sqlalchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'development.db')
    FLASK_ENV = 'development'
    FLASK_RUN_PORT = 9000


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'test.db')
    TESTING = True


config_class_name = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
