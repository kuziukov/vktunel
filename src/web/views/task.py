from flask import render_template, redirect, url_for, g
from decorators.login_required import login_required
from models.tasks import Tasks
from objects.vk_api import VKApi, VKApiResponse
from extentions.celery import download_album


@login_required
def task_page():
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
    tasks.album_name = dict(albums).get('title')

    tasks.save()

    print(community_id, album_id)

    res = download_album(user_id=str(g.user.id), community_id=community_id, album_id=album_id)
    print(res)

    return redirect(url_for('web.albums', community_id=community_id))
