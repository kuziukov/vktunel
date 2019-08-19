from cores.marshmallow_core import ApiSchema, fields


class FileSchema(ApiSchema):

    contentType = fields.Str()
    filename = fields.Str()
    length = fields.Str()
    uploadDate = fields.Timestamp()
    md5 = fields.Str()


class TaskSchema(ApiSchema):

    id = fields.Str(default=None)
    album_name = fields.Str(default=None)
    archive = fields.Nested(FileSchema, default=None)
    created_at = fields.Timestamp()

