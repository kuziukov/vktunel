import requests
from vk.utils import (
    json_iter_parse
)
from vk.exceptions import VkAPIError
from vk.methods import (
    APINamespace
)


class APIBase(object):
    METHOD_COMMON_PARAMS = {'v', 'lang', 'https', 'test_mode'}

    API_URL = 'https://api.vk.com/method/'
    CAPTCHA_URL = 'https://m.vk.com/captcha.php'

    def __new__(cls, *args, **kwargs):
        method_common_params = { key: kwargs.pop(key) for key in tuple(kwargs) if key in cls.METHOD_COMMON_PARAMS}
        api = object.__new__(cls)
        api.__init__(*args, **kwargs)
        return APINamespace(api, method_common_params)

    def __init__(self, timeout=10):
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers['Accept'] = 'application/json'
        self.session.headers['Content-Type'] = 'application/x-www-form-urlencoded'

    def send(self, request):
        self._prepare_request(request)
        method_url = self.API_URL + request.method
        response = self.session.post(method_url, request.method_params, timeout=self.timeout)
        response.raise_for_status()

        for response_or_error in json_iter_parse(response.text):
            request.response = response_or_error

            if 'response' in response_or_error:
                return response_or_error['response']
            elif 'error' in response_or_error:
                api_error = VkAPIError(request.response['error'])
                request.api_error = api_error
                return self.handle_api_error(request)

    def _prepare_request(self, request):
        request.method_params['access_token'] = self.access_token

    def get_access_token(self):
        raise NotImplementedError

    def handle_api_error(self, request):

        api_error_handler_name = 'on_api_error_' + str(request.api_error.code)
        api_error_handler = getattr(self, api_error_handler_name, self.on_api_error)

        return api_error_handler(request)

    def on_api_error(self, request):
        print(f'API error: {request.api_error}')
        raise request.api_error


class API(APIBase):
    def __init__(self, access_token, **kwargs):
        super().__init__(**kwargs)
        self.access_token = access_token




