import requests


class VKApi(object):

    def url(self, method, access_token, parameters):
        return f'https://api.vk.com/method/{method}' \
            f'?{parameters}' \
            f'&access_token={access_token}&v=5.95'


class VKApiResponse(object):
    @staticmethod
    def response(link) -> dict:
        response = requests.get(link)
        return response.json()
