from flask import render_template

from ..core import core


def redis():
    from .. import redis_store
    return redis_store


@core.route('/', methods=['GET', ])
def index():
    obj_id = id(redis())
    redis().hset(obj_id, "teste", "123")
    return render_template('index.html')
