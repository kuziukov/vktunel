from flask import request, current_app, jsonify
from functools import partial
from werkzeug.exceptions import HTTPException
from . import codes
from .exceptions import APIException


class Api:

    def __init__(self, blueprint):
        self.blueprint = blueprint
        self.blueprint.record(self._deferred_blueprint_init)

    def add_resource(self, resource, *urls, **kwargs):
        endpoint = kwargs.pop('endpoint', None) or resource.__name__.lower()
        resource.endpoint = endpoint
        resource_func = resource.as_view(endpoint)
        for url in urls:
            self.blueprint.add_url_rule(url, view_func=resource_func)
        return

    def _deferred_blueprint_init(self, setup_state):
        setup_state.app.handle_exception = partial(self.error_router, setup_state.app.handle_exception)
        setup_state.app.handle_user_exception = partial(self.error_router, setup_state.app.handle_user_exception)

    def error_router(self, original_handler, err):
        if self.blueprint.url_prefix is None:
            return self.handle_error(err)
        elif request.path.startswith(self.blueprint.url_prefix):
            return self.handle_error(err)
        return original_handler(err)

    @staticmethod
    def handle_error(err):
        if isinstance(err, HTTPException):
            message = err.description
            code = err.code
            error = err.__class__.__name__
        elif isinstance(err, APIException):
            message = err.message
            code = err.code
            error = err.__class__.__name__
        else:
            current_app.logger.error(err, exc_info=True)
            message = 'Internal Server Error.'
            code = codes.INTERNAL_SERVER_ERROR
            error = 'InternalServerError'

        data = {
            'code': code,
            'status': codes.get_status(code),
            'result': {
                'error': error,
                'message': message,
            }
        }
        resp = jsonify(data)
        resp.status_code = code
        return resp
