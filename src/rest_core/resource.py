from functools import wraps
from flask import (
    current_app,
    jsonify,
    request,
    g
)
from flask.views import MethodView
from . import codes


def format_results(function):

    @wraps(function)
    def wrapped(*args, **kwargs):
        result = function(*args, **kwargs)

        if isinstance(result, tuple):
            data, code = result
        else:
            data = result
            code = codes.OK

        data = {
            'status': codes.get_status(code),
            'code': code,
            'result': data,
        }
        resp = jsonify(data)
        resp.status_code = code
        return resp

    return wrapped


class Resource(MethodView):

    decorators = [format_results]

    @property
    def app(self):
        return current_app

    @property
    def config(self):
        return current_app.config

    @property
    def logger(self):
        return current_app.logger

    @property
    def request(self):
        return request

    @property
    def g(self):
        return g
