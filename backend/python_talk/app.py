from flask import Flask

from exts import db, cors, migrate

import config
import models

app = Flask(__name__)
app.config.from_object(config)

# 第三方扩展初始化
db.init_app(app)
cors.init_app(app)
migrate.init_app(app, db)


@app.get('/')
def index():
    return 'Python Talk!'
