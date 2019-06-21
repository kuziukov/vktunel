from flask import redirect
from objects.vk_auth import VKAuth


def login():

    auth = VKAuth('friends')
    return redirect(auth.url)

