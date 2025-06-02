
from celery import Celery as Celery_


class Celery(Celery_):

    def init_app(self, flask_app=None):
        self.conf.update(flask_app.config['CELERY_CONFIG'])
        self.Task = create_context_task(flask_app, self.Task)
        flask_app.celery = self


def create_context_task(flask_app, base_task_class):

    class ContextTask(base_task_class):
        def __call__(self, *args, **kwargs):
            with flask_app.app_context():
                return self.run(*args, **kwargs)

    return ContextTask
