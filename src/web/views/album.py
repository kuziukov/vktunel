from flask import render_template, g
from decorators.login_required import login_required
from objects.vk_api import VKApi, VKApiResponse
from datetime import datetime


@login_required
def album_page(community_id):

    community = VKApi().url(method='groups.getById', access_token=g.user.access_token, parameters=f'group_id={community_id}')
    community_response = VKApiResponse.response(community)
    community_response = community_response['response'][0]

    api = VKApi().url(method='photos.getAlbums', access_token=g.user.access_token, parameters=f'owner_id=-{community_id}&need_covers=1')
    response = VKApiResponse.response(api)
    communities = response['response']

    albums = communities['items']
    count = communities['count']

    return render_template('album_page.html', albums=albums, count=count, datetime=datetime, community=community_response)
