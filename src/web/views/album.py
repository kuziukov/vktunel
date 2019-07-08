from flask import render_template, g
from datetime import datetime
from cores.vk import API
from cores.vk import VkAPIError
from api.auth.decorators import web_login_required


@web_login_required
def album_page(community_id):

    api = API(g.user.access_token, v=5.95)

    community = api.groups.getById(group_id=community_id)[0]
    try:
        response = api.photos.getAlbums(owner_id=f'-{community_id}', need_covers=1)
        albums = response['items']
        count = response['count']
    except VkAPIError:
        albums = []
        count = 0

    return render_template('album_page.html', albums=albums, count=count, datetime=datetime, community=community)
