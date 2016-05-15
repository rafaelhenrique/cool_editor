from flask import render_template, redirect, url_for

from cool_editor.core import core_blueprint
from cool_editor.core.utils import id_generator


def redis():
    from .. import redis_store
    return redis_store


@core_blueprint.route('', methods=['GET', ])
def index():
    hashkey = id_generator()
    return redirect(url_for('core.editor', hashkey=hashkey))


@core_blueprint.route('editor/<hashkey>')
def editor(hashkey):
    redis().hset(hashkey, "teste", "123")
    return render_template('index.html')
