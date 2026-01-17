import marshmallow as ma


class MenuSchema(ma.Schema):
    # 虽然 model 中的 id 数据类型是 BigInteger, 但是 fields 中没有 BigInteger， 依然用 Int
    id = ma.fields.Integer(dump_only=True)
    url = ma.fields.String()
    name = ma.fields.String()
    parent_id = ma.fields.Integer()
    parent = ma.fields.Nested('MenuSchema',  exclude=('children',))
    # children 有多个，所以用 list
    children = ma.fields.List(ma.fields.Nested('MenuSchema',  exclude=('parent',)))


class MenuQueryArgsSchema(ma.Schema):
    name = ma.fields.String()
