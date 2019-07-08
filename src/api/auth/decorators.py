from functools import wraps
from flask import request, g, redirect, url_for
from jwt import DecodeError, ExpiredSignatureError
from mongoengine import DoesNotExist, ValidationError
from .jwt import Token
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
        token = request.headers.get('X-Auth-Token')
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


def web_login_required(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        cookie = request.cookies.get('access_token')
        if cookie is None:
            return redirect(url_for('web.index'))

        try:
            token, expire = Token.parse(cookie)
        except (DecodeError, ExpiredSignatureError):
            return redirect(url_for('web.index'))

        try:
            g.user = Users.objects.get(id=token.user_id)
        except (DoesNotExist, ValidationError):
            g.user = None

        return func(*args, **kwargs)
    return wrapped
