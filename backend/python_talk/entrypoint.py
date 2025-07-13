from python_talk.app import create_app

app = create_app()
# celery = app.celery

if __name__ == '__main__':
    print(app.url_map)
    app.run()