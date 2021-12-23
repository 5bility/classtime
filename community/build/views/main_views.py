from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return 'Hello, Pybo'

@bp.route('/community')
def community():
    return render_template('community.html')

@bp.route('/post')
def post():
    return render_template('post.html')