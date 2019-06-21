import logging


def init_logging(app):
    logging.basicConfig(filename='error.log', level=logging.DEBUG)
    return
