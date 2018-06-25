"""
Views of the Flask application.
"""
# pylint: skip-file
from flask import Blueprint, render_template

home = Blueprint('home', __name__)


@home.route('/', methods=['GET'])
def index():
    """
    Say hello using a template file.
    """
    return render_template('index.html')
