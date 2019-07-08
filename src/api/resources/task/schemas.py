from marshmallow_core import ApiSchema, fields


class TaskSchema(ApiSchema):

    id = fields.Str(default=None)
    album_name = fields.Str(default=None)
    archive = fields.BoolFile(default=False)
    created_at = fields.Timestamp()