from cores.marshmallow_core import ApiSchema
from cores.marshmallow_core import fields


class AlbumSchema(ApiSchema):

    id = fields.Str(default=None)
    title = fields.Str(default=None)
    created = fields.Int(default=None)