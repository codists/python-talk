from decimal import Decimal
from typing import Optional, List
from datetime import date

# Numeric 等数据类型
from sqlalchemy import Numeric
from sqlalchemy.orm import Mapped, mapped_column

from python_talk.extensions import db
from python_talk.models.base import PkModel, ModelMixin

book_author = db.Table(
    'book_author',
    db.Column('book_id', db.ForeignKey('book.id'), primary_key=True, nullable=False),
    db.Column('author_id', db.ForeignKey('author.id'), primary_key=True, nullable=False)
)


class Author(PkModel, ModelMixin):
    __tablename__ = 'author'

    # 因为使用 MySQL, 所以需要指定长度 db.String(128)，参考：- ：https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.String
    name: Mapped[str] = mapped_column(db.String(128), nullable=False)
    books: Mapped[List['Book']] = db.relationship(secondary=book_author, back_populates='authors')

    def __repr__(self):
        return f'<Author {self.name}>'


class Book(PkModel, ModelMixin):
    __tablename__ = 'book'

    title: Mapped[str] = mapped_column(db.String(128), nullable=False)
    isbn: Mapped[str] = mapped_column(db.String(128), unique=True, nullable=False, index=True)
    price: Mapped[Decimal] = mapped_column(Numeric(20, 2))
    # 默认可以为空
    description: Mapped[Optional[str]] = mapped_column(db.Text, default=None)
    url: Mapped[str] = mapped_column(db.String(255), nullable=False)
    # back_populates='book' 的 book 是 Author 模型里面的字段 book。
    authors: Mapped[List['Author']] = db.relationship(secondary=book_author,back_populates='books')
    publisher: Mapped[Optional[str]] = mapped_column(db.String(255), nullable=True)
    publication_date: Mapped[Optional[date]] = mapped_column(db.Date, nullable=True)

    def __repr__(self):
        return f'<Book {self.title}>'


