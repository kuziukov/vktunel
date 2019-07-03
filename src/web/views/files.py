from flask import make_response, Response, stream_with_context, current_app, g
from gridfs import GridFSBucket
from mongoengine import DoesNotExist, ValidationError
from pymongo import MongoClient
from werkzeug.exceptions import NotFound
from models.tasks import Tasks


def generate_archive(archive):
    for chunk in archive.get():
        yield chunk


def file_download(task_id):
    try:
        task = Tasks.objects(id=task_id).first()
    except (DoesNotExist, ValidationError):
        raise NotFound()

    if task.archive is None:
        raise NotFound()

    filename = 'archive.zip'

    headers = {
        'Content-Type': task.archive.content_type,
        'Content-Disposition': f'attachment; filename={filename}'
    }

    return Response(stream_with_context(generate_archive(task.archive)), headers=headers, direct_passthrough=True)





