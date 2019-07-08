from flask import (
    request,
    redirect,
    url_for,
    make_response
)
from mongoengine import NotUniqueError
from cores.objects import (
    VKAccess,
    VKAccessResponse
)
from models import Users
from api.auth.session import (
    create_session
)
from api.auth.token import Token
from cores.vk import API


def callback():
    code = request.args.get('code')

    token = VKAccess(code)
    response = VKAccessResponse.access(token)

    users = Users()
    users.access_token = response['access_token']
    expires_in = 2629744 if response['expires_in'] == 0 else response['expires_in']
    users.user_id = str(response['user_id'])

    api = API(users.access_token, v=5.95)
    response = api.users.get()[0]

    users.name = f'{response["first_name"]} {response["last_name"]}'

    try:
        users.save()
    except NotUniqueError:
        users = Users.objects.get(user_id=users.user_id)

    session = create_session(users=users, expires_in=expires_in)
    access_token, expires_in = Token(session_id=session.key, user_id=users.id).generate(expires_in)

    response = make_response(redirect(url_for('web.index')))
    response.set_cookie('access_token', access_token)
    return response


