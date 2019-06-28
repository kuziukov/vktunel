from mongoengine import (
    Document,
    StringField,
    BooleanField,
    FileField,
    DateTimeField
)
from datetime import datetime


class Tasks(Document):
    user_id = StringField(required=True)
    status = BooleanField(required=True, default=False)
    community_id = StringField(required=True)
    album_id = StringField(required=True)
    album_name = StringField(required=True)
    src = StringField(default=None)
    archive = FileField()
    created_at = DateTimeField(default=datetime.now)

    meta = {
        'collection': 'tasks'
    }
