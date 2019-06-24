from flask import (
    request,
    redirect,
    url_for,
    make_response
)
from mongoengine import NotUniqueError
from objects.vk_access import (
    VKAccess,
    VKAccessResponse
)
from objects.vk_api import (
    VKApi,
    VKApiResponse
)
from models import Users
from auth.session import (
    create_session
)
from auth.jwt import Token


def callback():
    code = request.args.get('code')

    token = VKAccess(code)
    response = VKAccessResponse.access(token)
    print(response)

    users = Users()
    users.access_token = response['access_token']
    users.expires_in = response['expires_in']
    users.user_id = str(response['user_id'])

    api = VKApi()
    url = api.url('users.get', users.access_token, '')

    response = VKApiResponse.response(url)

    users.name = f'{response["response"][0]["first_name"]} {response["response"][0]["last_name"]}'

    # expire = datetime.utcnow(), datetime.utcnow() + timedelta(seconds=86400)

    try:
        users.save()
    except NotUniqueError:
        print('Authorized')

    session = create_session(users=users, expires_in=users.expires_in)
    access_token, expires_in = Token(session_id=session.key, user_id=users.id).generate(users.expires_in)

    print(access_token)

    response = make_response(redirect(url_for('web.index')))
    response.set_cookie('access_token', access_token)
    return response


