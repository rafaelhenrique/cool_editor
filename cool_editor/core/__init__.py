from flask import Blueprint

core = Blueprint('core', __name__, template_folder='templates')

from ..core import views
