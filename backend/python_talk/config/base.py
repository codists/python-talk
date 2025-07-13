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
OPENAPI_URL_PREFIX = '/api' # 决定 openapi.json 文件的访问路径, 默认是 None
OPENAPI_JSON_PATH = 'openapi.json'
# Path to the Swagger UI page, relative to the base path. 默认是 None, 示例：
OPENAPI_SWAGGER_UI_PATH = 'docs'
# 如果使用 https://cdn.jsdelivr.net/npm/swagger-ui-dist/， 只有有网络的时候才可以使用
OPENAPI_SWAGGER_UI_URL = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
# ====================flask-smorest end====================


# ====================flask-sqlalchemy start====================
SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
# ====================flask-sqlalchemy end====================

