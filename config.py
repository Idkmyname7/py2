import os

class Config(object):
    # Flask config
    DEBUG = True

    # Database config
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:P@$$vv0RD@localhost:5432/For_Python'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Log files config
    LOG_FILES_DIR = '/var/log/apache2'
    LOG_FILES_PATTERN = 'access.log*'