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

    # 获取当前模块的顶级包名
    base_dir = __name__.split(".")[0]  # 如: 'src'
    flask_env = os.environ.get("FLASK_ENV", "development")
    # 动态导入配置文件模块
    config = importlib.import_module(f"{base_dir}.config.{flask_env}")

    app.config.from_object(config)