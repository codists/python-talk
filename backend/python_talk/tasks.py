from flask import current_app
from flask_mail import Message

from python_talk.extensions import  mail


# @celery.task
# def hello_world():
#     """
#     for the purpose of testing
#     """
#     print('hello world, current_app', current_app)  # 应用上下文可以访问 current_app/ g 请求上下文可以访问 request
#     print('Hello World')
#
#
# @celery.task
# def async_send_email():
#     msg = Message(recipients=['952328342@qq.com'])
#     mail.send(msg)
