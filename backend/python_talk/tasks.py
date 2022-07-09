# from python_talk.entrypoint import cel
from celery import current_app as celery


@celery.task
def hello_world():
    print('Hello World')
