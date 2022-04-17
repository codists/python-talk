import secrets

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@db:3306/python_talk?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 用于生成JWT
SECRET_KEY = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
ALGORITHM = 'HS256'

