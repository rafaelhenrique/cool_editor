from flask import render_template, redirect, url_for, jsonify
from flask_restful import Resource, reqparse

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
    redis().hset(hashkey, "status", "created")
    return render_template('index.html', hashkey=hashkey)


class Docs(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('key')
    parser.add_argument('value')

    def get(self, hashkey):
        document = redis().hgetall(hashkey)
        if not document:
            return 'Not found.', 404
        return jsonify(document)

    def put(self, hashkey):
        args = self.parser.parse_args()
        key, value = args.get('key'), args.get('value')
        if not key:
            return 'Bad request.', 400
        redis().hset(hashkey, key, value)
        return jsonify({hashkey: {key: value}})
