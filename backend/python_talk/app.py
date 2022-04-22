from flask import Flask, Blueprint

import config
import models  # noqa
from exts import db, cors, migrate
from utils.security import identify
from utils.restful import restful
from blueprints import user


app = Flask(__name__)
app.config.from_object(config)

# 第三方扩展初始化
db.init_app(app)
cors.init_app(app)
migrate.init_app(app, db)

# 注册蓝图
api = Blueprint('api', __name__, url_prefix='/api')
api.register_blueprint(user.user_bp)

# 获取token
app.before_request(identify)


@api.errorhandler(400)
def api_bad_request(error):
    return restful.error('Bad request'), 400


app.register_blueprint(api)


@app.get('/')
def index():
    return 'Python Talk!'
