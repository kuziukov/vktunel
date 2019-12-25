from flask import g
from api.auth.decorators import login_required
from cores.marshmallow_core import ApiSchema
from cores.marshmallow_core import fields
from cores.vk import API
from cores.rest_core import (
    Resource,
    APIException,
    codes
)
from utils.convert import from_link_get_id


class DeserializationSchema(ApiSchema):

    link = fields.Str(required=True)


class SerializationSchema(ApiSchema):

    type = fields.Str(default=None)
    object_id = fields.Str(default=None)


class LinkException(APIException):

    @property
    def message(self):
        return 'Invalid link, please try again later'

    code = codes.BAD_REQUEST


class UtilsLinkPost(Resource):

    @login_required
    def post(self):
        user = g.user
        data = DeserializationSchema().deserialize(self.request.json)

        object_id = from_link_get_id(data['link'])

        if not object_id:
            raise LinkException()

        api = API(user.access_token, v=5.95)

        try:
            utils = api.utils.resolveScreenName(screen_name=object_id)
        except Exception:
            raise LinkException()
        finally:
            if not utils:
                raise LinkException()

        return SerializationSchema().serialize(utils)
