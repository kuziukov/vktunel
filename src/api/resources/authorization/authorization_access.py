import requests
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

    token = fields.Str(required=True)


class AuthorizationAccessToken(Resource):

    def post(self):
        data = DeserializationSchema().deserialize(self.request.json)

        url = f"https://api.vk.com/method/secure.checkToken?v=5.101&token={ data['token'] }&client_secret=7DctKcRPCw28VykYBslv&access_token=dc433d99dc433d99dc1e615109dc287cb9ddc43dc433d99816565b8685fd16fbbbe1b44"

        print(url)
        response = requests.get(url)
        print(response.json())

        response = {
            'access_token': '1234'
        }

        return AuthorizationSchema().serialize(response)
