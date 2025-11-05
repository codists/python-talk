# @Filename: exceptions.py
# @Author: codists
# @Created: 2025-07-15 22:54:13

class BadRequestException(Exception):
    """Bad Request 异常
    :return:
    """
    status_code = 400

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __iter__(self):
        for k in ["message", "status_code"]:
            yield k, getattr(self, k)


