from marshmallow import EXCLUDE
from marshmallow.validate import Range
from api.auth.decorators import login_required
from api.resources.community.schemas import CommunitySchema
from cores.marshmallow_core import ApiSchema
from cores.marshmallow_core import fields
from cores.rest_core import Resource
from cores.vk import API


class FiltersSchema(ApiSchema):

    start = fields.Int(default=None, missing=0, validate=Range(min=0))
    limit = fields.Int(default=None, missing=50, validate=Range(min=0))
    start_time = fields.Timestamp(default=None)
    end_time = fields.Timestamp(default=None)


class SerializationSchema(ApiSchema):

    items = fields.Nested(CommunitySchema, many=True)
    totals = fields.Int()
    filters = fields.Nested(FiltersSchema)


class CommunityGet(Resource):

    @login_required
    def get(self):
        filters = FiltersSchema().deserialize(self.request.args, unknown=EXCLUDE)
        user = self.g.user

        query_kwargs = {}

        if 'start_time' in filters:
            query_kwargs['created_at__gte'] = filters['start_time']

        if 'end_time' in filters:
            query_kwargs['created_at__lte'] = filters['end_time']

        api = API(user.access_token, v=5.95)
        response = api.groups.get(extended=1)

        community = response['items']
        count = response['count']

        return SerializationSchema().serialize({'items': community, 'totals': count, 'filters': filters})
