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

    #   from datetime import datetime, timedelta
    #   print(datetime.utcnow(), datetime.utcnow() + timedelta(seconds=86400))

    return redirect(url_for('web.index'))

