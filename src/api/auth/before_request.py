from flask import (
    g,
    request
)
from jwt import DecodeError, ExpiredSignatureError
from mongoengine import DoesNotExist, ValidationError

from .token import Token
from models import Users
from models.tasks import Tasks


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

    try:
        task_count = Tasks.objects(user=g.user, archive__exists=False).count()
        g.tasks_in_works = task_count
    except (DoesNotExist, ValidationError):
        g.tasks_in_works = 0
        return


