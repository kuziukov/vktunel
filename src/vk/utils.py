import json
from collections import Iterable

STRING_LIKE_TYPES = (str, bytes, bytearray)


def stringify(value):
    if isinstance(value, Iterable) and not isinstance(value, STRING_LIKE_TYPES):
        return ','.join(map(str, value))
    return value


def stringify_values(dictionary):
    return {key: stringify(value) for key, value in dictionary.items()}


def json_iter_parse(response_text):
    decoder = json.JSONDecoder(strict=False)
    idx = 0
    while idx < len(response_text):
        obj, idx = decoder.raw_decode(response_text, idx)
        yield obj