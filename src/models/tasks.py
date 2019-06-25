from mongoengine import (
    Document,
    StringField,
    BooleanField
)


class Tasks(Document):
    user_id = StringField(required=True)
    status = BooleanField(required=True, default=False)
    community_id = StringField(required=True)
    album_id = StringField(required=True)
    album_name = StringField(required=True)
    src = StringField(default=None)

    meta = {
        'collection': 'tasks'
    }
