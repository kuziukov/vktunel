from flask import render_template, g
from decorators.login_required import login_required
from objects.vk_api import VKApi, VKApiResponse


@login_required
def community_page():

    api = VKApi().url(method='groups.get', access_token=g.user.access_token, parameters='extended=1')
    response = VKApiResponse.response(api)
    communities = response['response']

    community = communities['items']
    count = communities['count']

    return render_template('community_page.html', community=community, count=count)