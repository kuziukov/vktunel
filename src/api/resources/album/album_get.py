from marshmallow.validate import Range
from api.auth.decorators import login_required
from api.resources.album.schemas import AlbumSchema
from cores.marshmallow_core import ApiSchema
from cores.marshmallow_core import fields
from cores.rest_core import Resource, APIException, codes
from cores.vk import API, VkAPIError


class AccessDenied(APIException):

    @property
    def message(self):
        return 'Access denied: group photos are disabled'

    code = codes.BAD_REQUEST


class FiltersSchema(ApiSchema):

    start = fields.Int(default=None, missing=0, validate=Range(min=0))
    limit = fields.Int(default=None, missing=50, validate=Range(min=0))
    start_time = fields.Timestamp(default=None)
    end_time = fields.Timestamp(default=None)


class SerializationSchema(ApiSchema):

    items = fields.Nested(AlbumSchema, many=True)
    totals = fields.Int()
    filters = fields.Nested(FiltersSchema)


class AlbumGet(Resource):

    @login_required
    def get(self, community_id):
        user = self.g.user

        print(community_id)

        api = API(user.access_token, v=5.95)
        # community = api.groups.getById(group_id=community_id)[0]
        try:
            response = api.photos.getAlbums(owner_id=community_id, need_system=1, need_covers=1)
            albums = response['items']
            count = response['count']
        except VkAPIError:
            raise AccessDenied()

        return SerializationSchema().serialize({'items': albums, 'totals': count})
