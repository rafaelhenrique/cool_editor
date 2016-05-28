from flask import Blueprint
from flask_restful import Api

core_blueprint = Blueprint('core', __name__, template_folder='templates',
                           static_folder='static', static_url_path='core')
core_api = Api(core_blueprint)

from cool_editor.core import views  # noqa
core_api.add_resource(views.Docs, 'docs/<hashkey>')
