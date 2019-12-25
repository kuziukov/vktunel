from mongoengine import NotUniqueError
from api.auth.session import create_session
from api.auth.token import Token
from api.resources.authorization.schemas import AuthorizationSchema
from cores.marshmallow_core import (
    ApiSchema,
    fields
)
from cores.objects import (
    VKAccess,
    VKAccessResponse
)
from cores.vk import API
from models import Users
from cores.rest_core import (
    Resource,
    APIException,
    codes
)


class AuthorizationCodeException(APIException):

    @property
    def message(self):
        return 'Invalid Authorization Code'

    code = codes.BAD_REQUEST


class DeserializationSchema(ApiSchema):

    code = fields.Str(required=True)


class VkDeserializationSchema(ApiSchema):

    access_token = fields.Str(required=True)
    user_id = fields.Str(required=True)


class AuthorizationCode(Resource):

    def post(self):
        data = DeserializationSchema().deserialize(self.request.json)

        try:
            token = VKAccess(data['code'])
            response = VKAccessResponse.access(token)
        except Exception as e:
            self.logger.error(f'Failed to get access to VK: {str(e)}')

        if 'access_token' not in response and 'user_id' not in response:
            raise AuthorizationCodeException()

        access_token = response['access_token']
        user_id = str(response['user_id'])

        users = Users()
        users.access_token = access_token
        users.user_id = user_id

        if response['expires_in'] == 0:
            expires_in = 2629744
        else:
            expires_in = response['expires_in']

        api = API(users.access_token, v=5.95)
        response = api.users.get()[0]

        users.name = f'{response["first_name"]} {response["last_name"]}'

        try:
            users.save()
        except NotUniqueError:
            users = Users.objects.get(user_id=users.user_id)
            users.access_token = access_token
            users.save()
        except Exception as e:
            self.logger.error(f'Failed to save user to Database: {str(e)}')

        session = create_session(users=users, expires_in=expires_in)
        access_token, expires_in = Token(session_id=session.key, user_id=users.id).generate(expires_in)

        response = {
            'access_token': access_token,
            'expires_in': expires_in
        }

        return AuthorizationSchema().serialize(response)
