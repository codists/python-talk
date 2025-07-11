# @Filename: base.py
# @Author: codists
# @Created: 2025-07-11 15:00:22
import os

from dotenv import load_dotenv

load_dotenv()

# ====================flask-smorest start====================
API_TITLE='Python Talk 接口文档'
API_VERSION='v1'
# OpenAPI version 参考: https://spec.openapis.org/oas/latest.html
OPENAPI_VERSION='3.0.2'
# ====================flask-smorest end====================


# ====================flask-sqlalchemy start====================
SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
# ====================flask-sqlalchemy end====================

