# from python_talk.entrypoint import cel
from celery import current_app as celery


@celery.send_task
def hello_world():
    print('Hello World')
