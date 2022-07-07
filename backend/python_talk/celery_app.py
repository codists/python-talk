"""
1.flask中使用celery参考：https://flask.palletsprojects.com/en/latest/patterns/celery/
2.flask中使用celery主要是考虑app上下文： app1.app_context()
"""
from celery import Celery


def make_celery(app):
    celery = Celery(app.import_name)
    # 官方文档使用的是flask配置，这里使用celery单独的配置
    # celery.conf.update(app1.config["CELERY_CONFIG"])
    celery.config_from_object('celery_config')

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


class CeleryFactory(Celery):

    def init_app(self, flask_app):
        self.__init__(flask_app.import_name)
        self.config_from_object('celery_config')

        class ContextTask(self.Task):
            def __call__(self, *args, **kwargs):
                with flask_app.app_context():
                    return self.run(*args, **kwargs)

        self.Task = ContextTask
        return self
