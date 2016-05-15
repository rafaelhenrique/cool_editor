from flask import Blueprint

core = Blueprint('core', __name__, template_folder='templates',
                 static_folder='static', static_url_path='core')

from ..core import views  # noqa
