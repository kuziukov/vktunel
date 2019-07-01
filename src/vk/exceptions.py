
AUTHORIZATION_FAILED = 5
PERMISSION_IS_DENIED = 7
CAPTCHA_IS_NEEDED = 14
ACCESS_DENIED = 15
INVALID_USER_ID = 113


class VkException(Exception):
    pass


class VkAuthError(VkException):
    pass


class VkAPIError(VkException):

    CAPTCHA_NEEDED = 14
    ACCESS_DENIED = 15

    def __init__(self, error_data):
        super(VkAPIError, self).__init__()
        self.error_data = error_data
        self.code = error_data.get('error_code')
        self.message = error_data.get('error_msg')
        self.request_params = self.get_pretty_request_params(error_data)
        self.redirect_uri = error_data.get('redirect_uri')

    @staticmethod
    def get_pretty_request_params(error_data):
        request_params = error_data.get('request_params', ())
        request_params = {param['key']: param['value'] for param in request_params}
        return request_params

    def __str__(self):
        error_message = '{self.code}. {self.message}. request_params = {self.request_params}'.format(self=self)
        if self.redirect_uri:
            error_message += ',\nredirect_uri = "{self.redirect_uri}"'.format(self=self)
        return error_message


