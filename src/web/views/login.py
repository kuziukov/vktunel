from flask import redirect
from cores.objects import VKAuth


def login():
    auth = VKAuth('friends, photos, email, groups, offline')
    return redirect(auth.url)

