from mongoengine import NotUniqueError

from api.auth.decorators import login_required
from api.auth.session import create_session
from api.auth.token import Token
from api.resources.authorization.schemas import AuthorizationSchema
from cores.marshmallow_core import ApiSchema
from cores.marshmallow_core import fields
from cores.objects import VKAccess, VKAccessResponse
from cores.vk import API
from models import Users
from cores.rest_core import Resource, APIException, codes


class DeserializationSchema(ApiSchema):

    code = fields.Str(required=True)


class AuthorizationVkCode(Resource):

    def post(self):
        data = DeserializationSchema().deserialize(self.request.json)

        token = VKAccess(data['code'])
        response = VKAccessResponse.access(token)

        print(response)

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

        response = {
            'access_token': access_token
        }

        return AuthorizationSchema().serialize(response)
