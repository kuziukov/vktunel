from cores.marshmallow_core import ApiSchema
from cores.marshmallow_core import fields


class StreamSchema(ApiSchema):

    key = fields.Str(default=None)
    endpoint = fields.Str(default=None)


