from envparse import env

DEBUG = env.str('DEBUG')

MONGO_HOST = env.str('MONGO_HOST')
MONGO_PORT = env.int('MONGO_PORT')
MONGO_DBNAME = env.str('MONGO_DBNAME')

REDIS_HOST = env.str('REDIS_HOST')
REDIS_PORT = env.int('REDIS_PORT')

RABBIT_HOST = env.str('RABBIT_HOST')
RABBIT_PORT = env.int('RABBIT_PORT')
RABBIT_USER = env.str('RABBIT_USER')
RABBIT_PASS = env.str('RABBIT_PASS')

