from flask import Flask

import config
import models  # noqa
from exts import db, cors, migrate


app = Flask(__name__)
app.config.from_object(config)

# 第三方扩展初始化
db.init_app(app)
cors.init_app(app)
migrate.init_app(app, db)


@app.get('/')
def index():
    return 'Python Talk!'
