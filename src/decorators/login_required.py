from functools import wraps
from flask import (
    g,
    request,
    redirect,
    url_for,
    current_app
)


def login_required(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        cookie = request.cookies.get('access_token')
        if cookie is None:
            return redirect(url_for('web.index'))

        # try to decode jwt token

        print(cookie)

        print(g.user)

        current_app.g.user = '1234'

        return func(*args, **kwargs)
    return wrapped

