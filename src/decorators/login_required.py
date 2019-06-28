from functools import wraps
from flask import (
    g,
    request,
    redirect,
    url_for,
    current_app
)
from jwt import DecodeError, ExpiredSignatureError
from mongoengine import DoesNotExist, ValidationError

from auth.jwt import Token
from models import Users


def login_required(func):
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

