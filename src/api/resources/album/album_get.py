from marshmallow.validate import Range
from api.auth.decorators import login_required
from api.resources.album.schemas import AlbumSchema
from cores.marshmallow_core import ApiSchema
from cores.marshmallow_core import fields
from cores.rest_core import Resource
from cores.vk import API, VkAPIError


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

        api = API(user.access_token, v=5.95)
        community = api.groups.getById(group_id=community_id)[0]
        try:
            response = api.photos.getAlbums(owner_id=f'-{community_id}', need_covers=1)
            albums = response['items']
            count = response['count']
        except VkAPIError:
            albums = []
            count = 0

        return SerializationSchema().serialize({'items': albums, 'totals': count})
