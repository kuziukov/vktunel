from flask import (
    g,
    request,
    redirect,
    url_for,
    current_app
)

from auth import Token
from models import Users


def before_request():
    cookie = request.cookies.get('access_token')
    if cookie is None:
        return redirect(url_for('web.index'))

    # try to decode jwt token

    token, expire = Token.parse(cookie)

    if token:
        g.user = Users.objects.get(id=token.user_id)
    else:
        g.user = None
