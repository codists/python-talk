from flask import Blueprint
from python_talk.tasks import hello_world

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.get('/')
def test():
    print('test')
    hello_world.delay()
    return 'This is test'
