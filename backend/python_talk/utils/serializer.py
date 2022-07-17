"""
序列化工具

参考
Python          JSON
dict            object
tuple, list     array
str             string
int, float      number
bool            boolean
None            null

使用
from python_talk.utils.serializer import serializer

serializer(user, ['id', 'username', 'email'])

# 如果 fields 为空，会去读取模型类定义的 __serializer__
serializer(user)

# 指定某种类型统一序列化
serializer(user, funcs={
    datetime: lambda dt: dt.strftime('%Y-%m-%d %H:%M:%S')
})

# 自定义序列化后的格式
serializer(user, ['id'], funcs={
    'id': lambda id_: f'userId:{id_}'
})
"""

from datetime import datetime
from collections.abc import Iterable

__all__ = ['serializer', ]

BASE_TYPES = (
    dict,
    tuple, list,
    str,
    int, float,
    bool,
    type(None)
)

SERIALIZER = '__serializer__'
DATETIME_FORMATTER = '%Y-%m-%d %H:%M:%S'


def check_type(instance, types=BASE_TYPES):
    """
    判断实例是否属于某些类型（不包含它们的子类）
    注意与 isinstance 的区别
    """
    t = type(instance)
    for type_ in types:
        if t == type_:
            return True
    return False


class Serializer:

    def __init__(self, default_funcs=None):
        self.default_funcs = default_funcs or {
            datetime: lambda dt: dt.strftime(DATETIME_FORMATTER),
        }

    def __call__(self, instance_instances, fields=None, funcs=None):
        return self.serializer(instance_instances, fields, funcs)

    def serializer(self, instance_instances, fields=None, funcs=None, top=None):
        if isinstance(instance_instances, Iterable):
            return [self.serializer(instance, fields, funcs, top=top) for instance in instance_instances]

        instance = instance_instances
        fields = fields or getattr(instance, SERIALIZER, [])
        funcs = funcs or {}
        result = {}

        for field_name in fields:
            if isinstance(field_name, str):
                value = getattr(instance, field_name)
                func_key = f'{top}.{field_name}' if top else field_name
                func = funcs.get(func_key) or funcs.get(type(value)) or self.default_funcs.get(type(value))
                if func:
                    value = func(value)

                if not check_type(value):
                    value = self.serializer(value, funcs=funcs, top=field_name)

                result[field_name] = value

            elif isinstance(field_name, dict):
                for f, child_fields in field_name.items():
                    result[f] = self.serializer(getattr(instance, f), child_fields, funcs, top=f)

        return result


serializer = Serializer()
