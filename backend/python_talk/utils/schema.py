class Schema:

    def __init__(self, **kwargs):
        self.fields = [field_name for field_name, field in self.__class__.__dict__.items() if isinstance(field, Field)]
        for field_name in self.fields:
            if field_name in kwargs:
                setattr(self, field_name, kwargs[field_name])

    def __repr__(self):
        return f'<{self.__class__.__name__!r} {self.__dict__!r}>'

    def to_dict(self):
        return {field_name: getattr(self, field_name) for field_name in self.fields}

    def validate(self):
        pass


class Field:

    def __init__(self, request_field=None, default=None):
        self.__name = request_field
        self.__default = default

    def __set_name__(self, owner, name):
        if self.__name is None:
            self.__name = name

    def __get__(self, instance, owner=None):
        if not instance:
            return self
        return instance.__dict__.get(self.__name, self.__default)

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value

    def validate(self):
        pass


class StringField(Field):
    def __init__(self, request_field=None, default=''):
        super().__init__(request_field, default)
