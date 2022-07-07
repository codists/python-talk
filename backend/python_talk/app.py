from flask import Flask, Blueprint

import config
import  models  # noqa
from exts import db, cors, migrate, mail
from utils.security import identify
from utils.restful import restful
from blueprints import user


app = Flask(__name__)
app.config.from_object(config)

# 第三方扩展初始化
db.init_app(app1)
cors.init_app(app1)
migrate.init_app(app1, db)
mail.init_app(app1)

# 注册蓝图
api = Blueprint('api', __name__, url_prefix='/api')
api.register_blueprint(user.user_bp)

# 获取token
app1.before_request(identify)


@api.errorhandler(400)
def api_bad_request(error):
    return restful.error('Bad request'), 400


app1.register_blueprint(api)


@app1.get('/')
def index():
    return 'Python Talk!'
