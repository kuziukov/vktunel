from mongoengine import (
    Document,
    StringField,
    FileField,
    DateTimeField,
    ReferenceField
)
from datetime import datetime
from .users import Users


class Tasks(Document):
    user = ReferenceField(Users, required=True)
    community_id = StringField(required=True)
    album_id = StringField(required=True)
    album_name = StringField(required=True)
    archive = FileField()
    created_at = DateTimeField(default=datetime.now)

    meta = {
        'collection': 'tasks'
    }
