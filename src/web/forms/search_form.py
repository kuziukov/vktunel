import re
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    validators,
    ValidationError
)


class SearchForm(FlaskForm):
    search = StringField('https://vk.com/fest')
