from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy import select

from python_talk.models.menu import Menu
from python_talk.schemas.menu import MenuSchema, MenuQueryArgsSchema
from python_talk.extensions import db

bp = Blueprint("menus", "menus", url_prefix="/api/menus", description="菜单栏")


@bp.route("/")
class Menus(MethodView):
    @bp.arguments(MenuQueryArgsSchema, location="query")
    @bp.response(200, MenuSchema(many=True))
    def get(self, args):
        """
        查询所有菜单
        """

        stmt = select(Menu)
        result = db.session.scalars(stmt).all()
        return result
