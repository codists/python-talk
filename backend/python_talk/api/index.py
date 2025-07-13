# @Filename: index.py
# @Author: codists
# @Created: 2025-07-12 14:43:00
"""
flask-smorest demo，仅用于测试
"""

from flask import render_template
from flask.views import MethodView
from flask_smorest import Blueprint

# Blueprint 第一个参数是 name, 第二个参数是 import_name
bp = Blueprint("index", __name__, url_prefix="/api", description="首页")


# 方式 1
# @bp.route("/index", methods=["GET"])
# @bp.response(200)
# def index():
#     """首页
#
#     """
#     ret = {
#         'data': 'welcome to Python Talk'
#     }
#     return ret


@bp.route("/", methods=["GET"])
class IndexView(MethodView):
    """首页

    """
    @bp.response(200)
    def get(self):
        """首页

        """
        ret = {
            'data': 'welcome to Python Talk'
        }
        return ret

@bp.route("/docs/local")
def specs():
    return render_template("swagger-ui.html")