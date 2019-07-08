from config import (
    CLIENT_ID,
    REDIRECT_URL
)


class VKAuth(object):

    def __init__(self, scope):
        self.client_id = CLIENT_ID
        self.redirect_url = REDIRECT_URL
        self.scope = scope

    @property
    def url(self) -> str:
        return f'https://oauth.vk.com/authorize' \
            f'?client_id={ self.client_id }' \
            f'&display=page' \
            f'&redirect_uri={ self.redirect_url }' \
            f'&scope={ self.scope }' \
            f'&response_type=code' \
            f'&v=5.95'
