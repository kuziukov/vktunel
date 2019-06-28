import os
import shutil
import urllib.request
from werkzeug.exceptions import Forbidden

from models import Users
from models.tasks import Tasks

from mongoengine import connect, DoesNotExist, ValidationError


class Size(object):
    def __init__(self, url, width, height, type):
        self.url = url
        self.width = width
        self.height = height
        self.type = type

    @property
    def name(self):
        return self.url.split('/')[-1]


class Photo(object):

    def __init__(self, id, album_id, owner_id, user_id, sizes, text, date):
        self.id = id
        self.album_id = album_id
        self.owner_id = owner_id
        self.user_id = user_id
        self._sizes = self._parse_list_of_size(sizes)
        self.text = text
        self.date = date

    def _parse_list_of_size(self, sizes):
        _list = []
        for value in sizes:
            _list.append(Size(**value))
        return _list

    @property
    def picture(self) -> Size or None:
        _chosen_picture = None
        type_of_sizes = ['w', 'z', 'y', 'x', 'm', 's']

        for value in type_of_sizes:
            for size in self._sizes:
                if size.type == value:
                    _chosen_picture = size
                    return _chosen_picture
        return None


class PhotoAlbum(object):

    def __init__(self):
        self.folder = 'files/albums/photo_album'
        self._listOfPhotos = []
        try:
            os.makedirs(self.folder)
        except FileExistsError:
            shutil.rmtree(self.folder, ignore_errors=True)
            self.__init__()

    def add(self, items):
        for item in items:
            self._listOfPhotos.append(Photo(**item))

    def count_in_list(self):
        return len(self._listOfPhotos)

    def download(self):

        for photo in self._listOfPhotos:
            urllib.request.urlretrieve(photo.picture.url, f'{self.folder}/{photo.picture.name}')

        shutil.make_archive(self.folder, 'zip', self.folder)

        archive = open(f'{self.folder}.zip', 'rb')
        return archive

    def __del__(self):
        shutil.rmtree(self.folder, ignore_errors=True)


connect(
    alias="default",
    db='vktunel',
    host='127.0.0.1',
    port=27017
)


try:
    user = Users.objects.get(id='5d0d072af34e9164d8e4cc7a')
except (DoesNotExist, ValidationError):
    user = None

if user is None:
    raise Forbidden()


from vk import API


community_id = '33264810'
album_id = '197699202'


api = API(user.access_token, v=5.95)
response = api.photos.get(owner_id=f'-{community_id}', album_id=album_id, count=50)


items = response['items']
count = response['count']


photoAlbum = PhotoAlbum()
photoAlbum.add(items)
archive = photoAlbum.download()

task = Tasks.objects.get(id='5d120a5c88dd9d8b201f5a56')
task.archive.put(archive, content_type='application/zip')
task.save()





