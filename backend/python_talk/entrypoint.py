from python_talk.app import create_app

app = create_app('development')
celery = app.celery
