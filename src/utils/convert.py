from datetime import date, timedelta

from flask import g
from cores.vk import API


def convert_url(url):
    data = url.split('/')

    if len(data) >= 4 and data[3]:
        mask = data[3]

        api = API(access_token=g.user.access_token, v=5.100)
        response = api.utils.resolveScreenName(screen_name=mask)

        if 'type' in response and 'object_id' in response:
            type = response['type']
            object_id = response['object_id']
            return object_id

    return None


def from_link_get_id(url):
    data = url.split('/')

    if len(data) >= 4 and data[3]:
        mask = data[3]
        return mask
    return None


def get_first_day(dt, d_years=0, d_months=0):
    y, m = dt.year + d_years, dt.month + d_months
    a, m = divmod(m-1, 12)
    return date(y+a, m+1, 1)


def get_last_day(dt):
    return get_first_day(dt, 0, 1) + timedelta(-1)