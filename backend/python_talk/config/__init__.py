# @Filename: __init__.py
# @Author: codists
# @Created: 2025-07-11 14:59:58

import importlib
import os

from . import base


def load(app):
    """
    根据环境（测试/开发/生产）加载配置

    """
    app.config.from_object(base)
    flask_env = os.environ.get("FLASK_ENV", "development")
    config = importlib.import_module("python_talk.config.%s" % flask_env)  # 动态导入配置文件模块
    app.config.from_object(config)