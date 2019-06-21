from flask_mongoengine import MongoEngine

mongo = None


def init_mongo(app):
    global mongo
    mongo = MongoEngine()
    mongo.init_app(app)
    return
