from python_talk.app import create_app
from python_talk.celery_app import make_celery

app = create_app('production')
celery_app = make_celery(app)
