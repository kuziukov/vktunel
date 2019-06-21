from flask import (
    request,
    redirect,
    url_for
)
from objects.vk_access import (
    VKAccess,
    VKAccessResponse
)


def callback():
    code = request.args.get('code')

    token = VKAccess(code)
    response = VKAccessResponse.access(token)
    print(response)

    return redirect(url_for('web.index'))

