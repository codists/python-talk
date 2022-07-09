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

    # send email
    MAIL_SERVER = 'smtp.163.com'
    MAIL_USERNAME = 'codists@163.com'
    MAIL_PASSWORD = ''
    MAIL_DEFAULT_SENDER = "默认发送人"
    MAIL_USE_SSL = True
    # MAIL_USE_TLS = False
    # MAIL_PORT = 465
    MAIL_PORT = 587

    # celery
    CELERY_CONFIG = {
        'broker_url': 'redis://localhost:6379/0',
        'result_backend': 'redis://localhost:6379/0'
    }


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    # turn on debug
    DATABASE_URI = prefix + os.path.join(basedir, 'dev.db')


class TestingConfig(Config):
    DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True


config_class_name = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
