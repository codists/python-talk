from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy import select

from python_talk.models.book import Book
from python_talk.schemas.book import BookSchema, BookQueryArgsSchema
from python_talk.extensions import db

bp = Blueprint("books", "books", url_prefix="/api/books", description="书籍")


@bp.route("/")
class Books(MethodView):
    @bp.arguments(BookQueryArgsSchema, location="query")
    @bp.response(200, BookSchema(many=True))
    def get(self, args):
        """
        查询所有菜单
        """

        stmt = select(Book)
        result = db.session.scalars(stmt).all()
        return result
