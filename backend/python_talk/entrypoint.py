import time
import subprocess

from backend.python_talk.app import app, db


def wait_db(application, database, interval=3):
    while True:
        try:
            with application.app_context():
                with database.engine.connect():
                    application.logger.info('[start flask] database connected.')
        except Exception as e:
            application.logger.warning('[start flask] wait db ...')
            application.logger.exception(e)
            time.sleep(interval)
        else:
            break


def run():
    wait_db(app, db)
    subprocess.run('flask db upgrade && flask run', shell=True)


if __name__ == '__main__':
    run()
