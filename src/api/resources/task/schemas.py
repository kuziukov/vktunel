from cores.marshmallow_core import ApiSchema
from cores.marshmallow_core import fields


class TaskSchema(ApiSchema):

    id = fields.Str(default=None)
    album_name = fields.Str(default=None)
    archive = fields.BoolFile(default=False)
    created_at = fields.Timestamp()