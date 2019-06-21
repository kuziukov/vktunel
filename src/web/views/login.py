from flask import redirect
from objects.vk_auth import VKAuth


def login():

    auth = VKAuth('friends, photos, email, groups, offline')
    return redirect(auth.url)

