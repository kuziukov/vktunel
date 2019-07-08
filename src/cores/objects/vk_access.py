import requests
from config import (
    CLIENT_ID,
    CLIENT_SECRET,
    REDIRECT_URL
)


class VKAccess(object):
    def __init__(self, code):
        self.client_id = CLIENT_ID
        self.client_secret = CLIENT_SECRET
        self.redirect_uri = REDIRECT_URL
        self.code = code

    @property
    def url(self) -> str:
        return f'https://oauth.vk.com/access_token' \
            f'?client_id={self.client_id}' \
            f'&client_secret={self.client_secret}' \
            f'&redirect_uri={self.redirect_uri}' \
            f'&code={self.code}'


class VKAccessResponse(object):
    @staticmethod
    def access(vk_access) -> dict:
        response = requests.get(vk_access.url)
        return response.json()
