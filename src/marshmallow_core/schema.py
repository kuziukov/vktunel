from marshmallow import (
    Schema as OriginSchema,
    ValidationError,
)
from rest_core.exceptions import DataError


class Schema(OriginSchema):

    def get_attribute(self, obj, attr, default):
        """
        https://github.com/marshmallow-code/marshmallow/blob/dev/src/marshmallow/schema.py#L400
        Переопределено поведение при сериализации обьекта. Сейчас при сериализация обьекта значение поля None считается
        неопределенным и его значение берется из параметра default если он определен, иначе поведение как в оригинале

        class S1(Schema):
            a = fields.Str(default='hello')

        class S2(Schema):
            b = fields.Nested(S1, default={})

        в оригинале:
        S1().dump({'b': None})
        {'b': None}

        сейчас:
        S1().dump({'b': None})
        {'b': {'a': 'hello'}}
        """
        value = super().get_attribute(obj, attr, default)
        if value is None:
            return default
        return value


class ApiSchema(Schema):

    def deserialize(self, data, many=None, unknown=None):
        try:
            data = self.load(data, many=many, unknown=unknown)
        except ValidationError as e:
            raise DataError(e.messages)
        return data

    def serialize(self, data, many=None):
        return self.dump(data, many=many)
