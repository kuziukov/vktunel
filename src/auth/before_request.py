from flask import (
    g,
    request
)
from jwt import DecodeError, ExpiredSignatureError
from mongoengine import DoesNotExist, ValidationError

from auth import Token
from models import Users


def before_request():
    cookie = request.cookies.get('access_token', None)
    if cookie is None:
        g.user = None
        return

    try:
        token, expire = Token.parse(cookie)
    except (DecodeError, ExpiredSignatureError):
        g.user = None
        return

    try:
        g.user = Users.objects.get(id=token.user_id)
    except (DoesNotExist, ValidationError):
        g.user = None
        return
