from python_talk.models.base import PkModel, ModelMixin
from python_talk.extensions import db

book_author = db.Table(
    'book_author',
    db.Column('book_id', db.ForeignKey('book.id'), primary_key=True, nullable=False),
    db.Column('author_id', db.ForeignKey('author.id'), primary_key=True, nullable=False)
)


class Author(PkModel, ModelMixin):
    __tablename__ = 'author'

    name = db.Column(db.String(128), nullable=False)
    book = db.relationship('Book', secondary=book_author, back_populates='author')

    def __repr__(self):
        return f'<Author {self.name}>'


class Book(PkModel, ModelMixin):
    __tablename__ = 'book'

    title = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(20), unique=True)
    price = db.Column(db.Numeric)
    description = db.Column(db.Text)
    url = db.Column(db.String(200))
    author = db.relationship('Author', secondary=book_author,back_populates='book')

    def __repr__(self):
        return f'<Book {self.title}>'


