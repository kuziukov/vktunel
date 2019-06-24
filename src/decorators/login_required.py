from functools import wraps
from flask import (
    g,
    request,
    redirect,
    url_for,
    current_app
)
from auth.jwt import Token
from models import Users


def login_required(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        cookie = request.cookies.get('access_token')
        if cookie is None:
            return redirect(url_for('web.index'))

        # try to decode jwt token

        token, expire = Token.parse(cookie)

        if token:
            g.user = Users.objects.get(id=token.user_id)

        return func(*args, **kwargs)
    return wrapped

