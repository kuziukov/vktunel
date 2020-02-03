from mongoengine import NotUniqueError
from api.auth.session import create_session
from api.auth.token import Token
from api.resources.authorization.schemas import (
    AuthorizationSchema,
    DeserializationSchema,
    VKDeserializationSchema,
    VKProfileSchema
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


class AuthorizationCode(Resource):

    def post(self):
        data = DeserializationSchema().deserialize(self.request.json)

        response = {}
        try:
            token = VKAccess(data['code'])
            response = VKAccessResponse.access(token)
        except Exception as e:
            self.logger.error(f'Failed to get access to VK: {str(e)}')

        try:
            from_vk_response = VKDeserializationSchema().deserialize(response)
        except Exception:
            raise AuthorizationCodeException()

        new_access_token = from_vk_response['access_token']
        users = Users()
        users.access_token = new_access_token
        users.user_id = str(from_vk_response['user_id'])

        api = API(users.access_token, v=5.95)
        try:
            response = api.users.get()[0]
        except Exception:
            raise AuthorizationCodeException()

        try:
            vkProfile = VKProfileSchema().deserialize(response, unknown='EXCLUDE')
        except Exception as e:
            raise AuthorizationCodeException()

        users.name = f'{vkProfile["first_name"]} {vkProfile["last_name"]}'

        try:
            users.save()
        except NotUniqueError:
            users = Users.objects.get(user_id=users.user_id)
            users.access_token = new_access_token
            users.save()
        except Exception as e:
            self.logger.error(f'Failed to save user to Database: {str(e)}')

        expires_in = 2629744 if from_vk_response['expires_in'] == 0 else from_vk_response['expires_in']
        session = create_session(
            users=users,
            expires_in=expires_in
        )
        access_token, expires_in = Token(session_id=session.key, user_id=users.id).generate(expires_in)

        return AuthorizationSchema().serialize({
            'access_token': access_token,
            'expires_in': expires_in
        })
