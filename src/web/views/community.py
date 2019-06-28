from flask import render_template, g
from decorators.login_required import login_required
from vk import API


@login_required
def community_page():

    api = API(g.user.access_token, v=5.95)
    response = api.groups.get(extended=1)

    community = response['items']
    count = response['count']

    return render_template('community_page.html', community=community, count=count)