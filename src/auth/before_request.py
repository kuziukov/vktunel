from flask import (
    g,
    request,
    redirect,
    url_for,
    current_app
)
from mongoengine import DoesNotExist, ValidationError

from auth import Token
from models import Users


def before_request():
    cookie = request.cookies.get('access_token', None)
    if cookie is None:
        g.user = None
        return

    token = None
    try:
        token, expire = Token.parse(cookie)
    except Exception:
        g.user = None

    if token:
        try:
            g.user = Users.objects.get(id=token.user_id)
        except (DoesNotExist, ValidationError):
            g.user = None
    else:
        g.user = None
