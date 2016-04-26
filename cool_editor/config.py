import os


class base_config(object):
    SITE_NAME = 'Cool Editor'
    MY_SALT = b"my preciousssssssssssssss"
    SECRET_KEY = os.urandom(24) + MY_SALT
    SERVER_NAME = os.environ.get('SERVER_NAME')
    LOGENABLE = True


class dev_config(base_config):
    DEBUG = True
    ASSETS_DEBUG = True
    WTF_CSRF_ENABLED = False


class test_config(base_config):
    TESTING = True
    WTF_CSRF_ENABLED = False


class prod_config(base_config):
    DEBUG = False
    ASSETS_DEBUG = False
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
