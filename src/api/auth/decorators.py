from functools import wraps
from flask import request, g
from jwt import DecodeError, ExpiredSignatureError
from mongoengine import DoesNotExist, ValidationError
from werkzeug.exceptions import Unauthorized

from auth import Token
from models import Users
from rest_core import APIException, codes


class UserNotAuthorized(APIException):

    @property
    def message(self):
        return 'Sorry, but user is not authorized, Please log in again.'

    code = codes.UNAUTHORIZED


def login_required(function):

    @wraps(function)
    def wrapped(*args, **kwargs):
        token = request.headers.get('access_token')
        if token is None:
            raise UserNotAuthorized()

        try:
            token, expire = Token.parse(token)
        except (DecodeError, ExpiredSignatureError):
            raise UserNotAuthorized()

        try:
            g.user = Users.objects.get(id=token.user_id)
        except (DoesNotExist, ValidationError):
            raise UserNotAuthorized()

        return function(*args, **kwargs)

    return wrapped
