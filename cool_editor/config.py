from decouple import config


class base_config(object):
    SITE_NAME = 'Cool Editor'
    SECRET_KEY = config('SECRET_KEY')
    SERVER_NAME = config('SERVER_NAME')
    LOGENABLE = True
    DEBUG = False


class dev_config(base_config):
    DEBUG = True
    ASSETS_DEBUG = True
    WTF_CSRF_ENABLED = False


class test_config(base_config):
    TESTING = True
    WTF_CSRF_ENABLED = False


class prod_config(base_config):
    ASSETS_DEBUG = False
    WTF_CSRF_ENABLED = True
