from flask import render_template

from ..core import core


@core.route('/', methods=['GET', ])
def index():
    return render_template('index.html')
