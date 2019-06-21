from envparse import env

DEBUG = env.str('DEBUG')

MONGO_HOST = env.str('MONGO_HOST')
MONGO_PORT = env.int('MONGO_PORT')
MONGO_DBNAME = env.str('MONGO_DBNAME')