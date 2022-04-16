from functools import partial


class Restful:
    @staticmethod
    def _format_response(status, message='', data=None):
        return {'status': status, 'message': message, 'data': data}

    success = partial(_format_response, 'success')
    error = partial(_format_response, 'error')


restful = Restful
