from python_talk.app import create_app

app = create_app('development')
celery = app.celery

if __name__ == '__main__':
    app.run(host='0.0.0.0')