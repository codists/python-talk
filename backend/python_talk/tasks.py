# from python_talk.entrypoint import cel
from flask import current_app

from python_talk.extensions import celery


@celery.task
def hello_world():
    print('hello world, current_app', current_app)  # 应用上下文可以访问 current_app/ g 请求上下文可以访问 request
    print('Hello World')
