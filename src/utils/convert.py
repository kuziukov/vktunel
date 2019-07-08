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

            if type == 'group':
                return object_id
    return None
