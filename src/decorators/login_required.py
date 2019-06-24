from functools import wraps
from flask import (
    g,
    request,
    redirect,
    url_for
)


def login_required(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        cookie = request.cookies.get('access_token')
        if cookie is None:
            return redirect(url_for('web.index'))

        # try to decode jwt token

        print(cookie)

        g.user = None

        return func(*args, **kwargs)
    return wrapped

