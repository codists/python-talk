# @Filename: base.py
# @Author: codists
# @Created: 2025-07-15 22:51:13

import logging
from typing import Any

from marshmallow import Schema, ValidationError

from python_talk.exceptions import BadRequestException

logger = logging.getLogger()


class BaseSchema(Schema):

    def handle_error(self, error: ValidationError, data: Any, *, many: bool, **kwargs):
        error_map = list(error.messages.values())[0] if many else error.messages
        for key, value in error_map.items():
            if isinstance(value, dict):
                value = list(value.values())[0]
            error_msg = f'验证错误, 错误字段为:{key} , 错误为:{";".join(value)}'
            logger.info(error_msg)
            raise BadRequestException(error_msg)

    class Meta:
        ordered = True
