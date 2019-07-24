from cores.marshmallow_core import (
    ApiSchema
)
from cores.marshmallow_core import fields


class CommunitySchema(ApiSchema):

    id = fields.Str(default=None)
    name = fields.Str(default=None)
    photo_50 = fields.Str(default=None)

