from flask import Flask, Blueprint

import config
import models  # noqa
from exts import db, cors, migrate
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
app.register_blueprint(api)


@app.get('/')
def index():
    return 'Python Talk!'
