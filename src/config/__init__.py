import os

from .env import (
    DEBUG,
    MONGO_PORT,
    MONGO_HOST,
    MONGO_DBNAME
)


## VK APP

CLIENT_ID = '7029024'
CLIENT_SECRET = '7DctKcRPCw28VykYBslv'
REDIRECT_URL = 'http://localhost:5000/callback'


MONGODB_SETTINGS = {
    'db': MONGO_DBNAME,
    'host': MONGO_HOST,
    'port': MONGO_PORT
}
