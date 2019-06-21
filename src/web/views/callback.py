from flask import (
    request,
    redirect,
    url_for
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

    try:
        users.save()
    except NotUniqueError:
        print('Authorized')

    #   from datetime import datetime, timedelta
    #   print(datetime.utcnow(), datetime.utcnow() + timedelta(seconds=86400))

    return redirect(url_for('web.index'))

