from mongoengine import (
    Document,
    StringField,
    IntField,
    EmbeddedDocumentField,
    EmbeddedDocument,
    BooleanField
)


class Limits(EmbeddedDocument):

    numberOfAlbums = IntField(required=True)
    numberOfPhotos = IntField(required=True)


class Plan(Document):
    number = IntField(required=True, unique=True)
    title = StringField(required=True)
    desc = StringField(required=True)
    price = IntField(required=True)
    limits = EmbeddedDocumentField(Limits)
    active = BooleanField(default=False)

    meta = {
        'collection': 'plans'
    }
