from flask import Blueprint

core_blueprint = Blueprint('core', __name__, template_folder='templates',
                           static_folder='static', static_url_path='core')

from cool_editor.core import views  # noqa
