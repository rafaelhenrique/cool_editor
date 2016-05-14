# import redis
from flask import Flask
from flask.ext.redis import FlaskRedis

from cool_editor import config
from cool_editor.core import core

redis_store = FlaskRedis()


def create_app(config=config.ProductionConfig):
    app = Flask("cool_editor")
    app.config.from_object(config)

    register_blueprints(app)
    register_errorhandlers(app)
    register_jinja_env(app)
    register_extensions(app)

    return app


def register_blueprints(app):
    app.register_blueprint(core, url_prefix='/')


def register_errorhandlers(app):
    def render_error(e):
        if e.code == 400:
            return 'Bad request.', 400
        elif e.code == 404:
            return 'Not found.', 404
        elif e.code == 500:
            return 'Internal server error', 500

    for e in [400, 404, 500]:
        app.errorhandler(e)(render_error)


def register_jinja_env(app):
    pass


def register_extensions(app):
    redis_store.init_app(app)
