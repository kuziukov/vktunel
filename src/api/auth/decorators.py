from flask import (
    request,
    g
)
from mongoengine import (
    DoesNotExist,
    ValidationError
)
from jwt import (
    DecodeError,
    ExpiredSignatureError
)
from functools import wraps

from api.auth.session import Session
from cores.rest_core import (
    APIException,
    codes
)
from .token import Token
from models import Users
from datetime import datetime


class UserNotAuthorized(APIException):

    @property
    def message(self):
        return 'Sorry, but user is not authorized, Please log in again.'

    code = codes.UNAUTHORIZED


class SubscriptionExpired(APIException):

    @property
    def message(self):
        return 'The subscription of the account is expired'

    code = codes.NOT_ALLOWED


def valid_subscription(function):

    @login_required
    def wrapped(*args, **kwargs):
        user = g.user

        try:
            if user.subscription.expired_on < datetime.utcnow() or user.subscription.paid is not True:
                raise SubscriptionExpired()
        except Exception:
            raise SubscriptionExpired()

        return function(*args, **kwargs)

    return wrapped


def login_required(function):

    @wraps(function)
    def wrapped(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token is None:
            raise UserNotAuthorized()

        try:
            token, expire = Token.parse(token)
        except (DecodeError, ExpiredSignatureError):
            raise UserNotAuthorized()

        session = Session(token.session_id)
        if not session.is_exists():
            raise UserNotAuthorized()

        try:
            g.user = Users.objects.get(id=token.user_id)
        except (DoesNotExist, ValidationError):
            raise UserNotAuthorized()

        return function(*args, **kwargs)

    return wrapped
