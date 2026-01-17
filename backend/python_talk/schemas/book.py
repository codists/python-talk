import marshmallow as ma


class AuthorSchema(ma.Schema):
    id = ma.fields.Integer(dump_only=True)
    name = ma.fields.String()
    # 多对多关系出现循环导入，所以使用字符串'BookSchema'，而不是 BookSchema
    books = ma.fields.Nested('BookSchema', many=True, exclude=('authors',))


class BookSchema(ma.Schema):
    id = ma.fields.Integer(dump_only=True)
    title = ma.fields.String()
    isbn = ma.fields.String()
    price = ma.fields.Decimal()
    description = ma.fields.String()
    url = ma.fields.String()
    authors = ma.fields.Nested('AuthorSchema', many=True, exclude=('books',))
    publisher = ma.fields.String()
    publication_date = ma.fields.Date()


class BookQueryArgsSchema(ma.Schema):
    name = ma.fields.String()
