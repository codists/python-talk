import re
from abc import ABC, abstractmethod

from flask import request, abort, make_response


class ArgumentError(Exception):
    def __init__(self, message):
        self.message = message


class ArgumentRequiredError(ArgumentError):
    pass


class ArgumentValidatorError(ArgumentError):
    pass


class ArgumentTypeConvertError(ArgumentError):
    pass


class BaseValidator(ABC):

    @abstractmethod
    def __call__(self, value):
        raise NotImplemented


class LengthValidator(BaseValidator):
    def __init__(self, min_len, max_len):
        self.min_len = min_len
        self.max_len = max_len

    def __call__(self, value):
        if self.min_len <= len(value) <= self.max_len:
            return
        raise ArgumentValidatorError(f'except length between {self.min_len} ~ {self.max_len}, but got {len(value)}')


class RangeValidator(BaseValidator):
    def __init__(self, min_, max_):
        self.min_ = min_
        self.max_ = max_

    def __call__(self, value):
        if self.min_ <= value <= self.max_:
            return
        raise ArgumentValidatorError(f'except range >= {self.max_} and <= {self.min_}, but got {value}')


class RegexValidator(BaseValidator):
    def __init__(self, regex, message=None):
        self.regex = regex
        self.message = message

    def __call__(self, value):
        if self.regex.match(value):
            return
        message = self.message(value) if callable(self.message) else self.message
        raise ArgumentValidatorError(message)


class EmailValidator(RegexValidator):
    def __init__(self, message='Illegal email format'):
        super().__init__(
            re.compile(r'^([a-zA-Z\d_\-.]+)@([a-zA-Z\d_\-.]+)\.([a-zA-Z]{2,5})$'),
            lambda value: f'{message}, got {value}'
        )


class Argument:
    def __init__(
            self,
            name,
            type_=str,
            required=False,
            default=None,
            location=('json',),
            validators=(),
            required_msg=None,
            type_msg=None,
    ):
        self.name = name
        self.type_ = type_
        self.required = required
        self.default = default
        self.location = location
        self.validators = validators
        self.required_msg = required_msg
        self.type_msg = type_msg

    def source(self):
        values = []

        for location in self.location:
            location_data = getattr(request, location)
            if self.name not in location_data:
                continue
            if hasattr(location_data, 'getlist'):
                values.extend(location_data.getlist(self.name))
            else:
                values.append(location_data[self.name])

        return values

    def parse(self):
        source = self.source()
        if not source:
            if self.required:
                msg = self.required_msg(self) if callable(self.required_msg) else f'{self.name} is required'
                raise ArgumentRequiredError(msg)

            source = [self.default]

        value = source[-1]

        try:
            value = self.type_(value)
        except (TypeError, ValueError):
            msg = self.type_msg(self, value) if callable(self.type_msg) \
                else f'expect {self.type_}, but got {value!r}'
            raise ArgumentTypeConvertError(msg)

        for validator in self.validators:
            validator(value)

        return value


class KeyAttributeDict(dict):
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(item)

    def __setattr__(self, key, value):
        self[key] = value


class RequestParser:
    def __init__(self):
        self.args = []

    def add_arg(self, name, type_=str, required=False, default=None, location='json', validators=(), required_msg=None,
                type_msg=None):
        if default is None:
            default = type_()

        if isinstance(location, str):
            location = (location,)

        self.args.append(Argument(name, type_, required, default, location, validators, required_msg, type_msg))

    def parse_args(self):
        result = KeyAttributeDict()
        messages = {}

        for arg in self.args:
            try:
                value = arg.parse()
            except ArgumentError as e:
                messages[arg.name] = e.message
            except Exception as e:
                messages[arg.name] = str(e)
            else:
                result[arg.name] = value

        if messages:
            response = make_response({
                'code': 4000,
                'message': messages,
            })
            response.status_code = 400
            abort(response)

        return result
