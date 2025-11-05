# @Filename: __init__.py
# @Author: codists
# @Created: 2025-07-12 14:38:39

import importlib
import os
from pathlib import Path

from python_talk.extensions import api


def register_blueprint():
    """注册蓝图

    """
    api_dir = Path(__file__).absolute().parent

    for name in os.listdir(api_dir):
        filename, suffix = os.path.splitext(name)

        # 过滤掉 __pycache__
        if suffix == ".py":
            api_mod = importlib.import_module("python_talk.api.%s" % filename)
            if hasattr(api_mod, "bp"):
                # 将 flask 应用的蓝图注册到 flask-smorest api 上
                api.register_blueprint(getattr(api_mod, "bp"))