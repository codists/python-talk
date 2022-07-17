from datetime import datetime
from collections.abc import Iterable

"""
Python          JSON
dict            object
tuple, list     array
str             string
int, float      number
bool            boolean
None            null
"""

BASE_TUPLES = (
    dict,
    tuple, list,
    str,
    int, float,
    bool,
    type(None)
)

SERIALIZER = '__serializer__'

DATETIME_FORMATTER = '%Y-%m-%d %H:%M:%S'


def __check_type(instance, types=BASE_TUPLES):
    """
    判断实例是否属于某些类型（不包含它们的子类）
    注意与 isinstance 的区别
    """
    t = type(instance)
    for type_ in types:
        if t == type_:
            return True
    return False


def serializer(instance_instances, fields=None, funcs=None):
    """
    Usage:
        user = User.query.get(1)
        serializer(user, ['username', {'articles': ['id', 'title']}])
    or  serializer(user, ['username', 'created_at'], {datetime: lambda dt: dt.strftime('%Y-%m-%d')})
    """
    if isinstance(instance_instances, Iterable):
        return [serializer(instance, fields) for instance in instance_instances]

    instance = instance_instances
    fields = fields or getattr(instance, SERIALIZER, [])
    funcs = funcs or {}
    funcs.update({datetime: lambda dt: dt.strftime(DATETIME_FORMATTER)})

    result = {}

    for field_name in fields:
        if isinstance(field_name, str):
            field_value = getattr(instance, field_name)
            if not __check_type(field_value):
                func = funcs.get(field_name) or funcs.get(type(field_value))
                field_value = func(field_value) if func else serializer(field_value)

            result[field_name] = field_value

        elif isinstance(field_name, dict):
            for f, child_fields in field_name.items():
                child = getattr(instance, f)
                result[f] = serializer(child, child_fields)

    return result
