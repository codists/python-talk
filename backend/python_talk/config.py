"""
flask配置参考：
"""
import os

# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@db:3306/python_talk?charset=utf8'
SQLALCHEMY_DATABASE_URI = "sqlite:///test.sqlite"

# 问题：相对路径如何表示
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 用于生成JWT
SECRET_KEY = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
ALGORITHM = 'HS256'

# 邮件配置
# 谷歌邮箱端口：587， 网易邮箱端口：25， QQ邮箱端口：
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'codists@163.com'
MAIL_PASSWORD = 'KFUQPGLXRYVMWZMG'
# MAIL_DEFAULT_SENDER = 'noreply@pythontalk.com'
MAIL_DEFAULT_SENDER = 'codists@163.com'


"""
celery配置文件参考：https://docs.celeryq.dev/en/stable/userguide/configuration.html
"""

# Broker settings.
# broker_url = 'amqp://guest:guest@localhost:5672//'
broker_url = 'redis://localhost:6379/1'

# Using the database to store task state and results.
result_backend = 'redis://localhost:6379/2'
