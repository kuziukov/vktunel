from mongoengine import (
    Document,
    StringField
)


class Users(Document):
    user_id = StringField(required=True, unique=True)
    name = StringField(required=True)
    access_token = StringField(required=True)

    meta = {
        'collection': 'users'
    }
