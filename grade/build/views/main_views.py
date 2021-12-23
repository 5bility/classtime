from flask import Blueprint, render_template

from build.models import Grade

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return 'Hello, Pybo'

@bp.route('/grade')
def grade():
    grade_list = Grade.query.order_by(Grade.id)
    return render_template('grade.html')