import os

from .env import (
    DEBUG,
    MONGO_PORT,
    MONGO_HOST,
    MONGO_DBNAME,
    MONGO_USER,
    MONGO_PASSWORD,
    REDIS_PORT,
    REDIS_HOST,
    REDIS_PASSWORD,
    RABBIT_HOST,
    RABBIT_PORT,
    RABBIT_USER,
    RABBIT_PASS,

)


## VK APP

CLIENT_ID = '7029024'
CLIENT_SECRET = '7DctKcRPCw28VykYBslv'
REDIRECT_URL = 'http://localhost:8080/callback'


MONGODB_SETTINGS = {
    'db': MONGO_DBNAME,
    'host': MONGO_HOST,
    'port': MONGO_PORT,
    'username': MONGO_USER,
    'password': MONGO_PASSWORD
}

SECRET_KEY = '0bde8eef5dc532bc3d88e6c2caf5d3cb27b7d591d0cbb5941d7676a2798369a969cf8a6'


SESSION_STORE_URL = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0'
NOTIFICATION_STORE_URL = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/1'


CELERY_SETTINGS = dict(
    BROKER_URL=f'amqp://{RABBIT_USER}:{RABBIT_PASS}@{RABBIT_HOST}:{RABBIT_PORT}//',
    CELERY_ROUTES={
        'download-album': {'queue': 'common'},
        'fcm-notification': {'queue': 'common'},
    },
)

