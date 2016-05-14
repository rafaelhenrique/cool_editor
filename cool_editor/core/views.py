from flask import render_template

from ..core import core


@core.route('/', methods=['GET', ])
def index():
    from .. import redis_store
    redis_store.hset(id(redis_store), "teste", "123")
    return render_template('index.html')
