from flask import render_template, redirect, url_for, g
from decorators.login_required import login_required
from models.tasks import Tasks
from objects.vk_api import VKApi, VKApiResponse


@login_required
def task_page():
    print(g.user.id)

    tasks = Tasks.objects(user_id=str(g.user.id)).all()

    return render_template('task_page.html', tasks=tasks)


@login_required
def task_post(community_id, album_id):

    api = VKApi().url(method='photos.getAlbums', access_token=g.user.access_token,
                      parameters=f'owner_id=-{community_id}&need_covers=1&album_ids={album_id}')
    response = VKApiResponse.response(api)
    communities = response['response']
    albums = communities['items'][0]

    tasks = Tasks()
    tasks.community_id = community_id
    tasks.album_id = album_id
    tasks.user_id = str(g.user.id)
    tasks.status = False
    tasks.src = None
    tasks.album_name = dict(albums).get('title')

    tasks.save()

    print(community_id, album_id)
    return redirect(url_for('web.albums', community_id=community_id))
