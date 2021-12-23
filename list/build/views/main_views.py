from flask import Blueprint, render_template

from build.models import Lecture, Evaluation, Professor
from build.app import db

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def hello_pybo():
    return 'Hello, Pybo'

@bp.route('/list')
def index():
    class_list = db.session.query(Lecture.name, Lecture.classroom, Lecture.classtime, Lecture.student_count, Professor.name.label('prof_name')).filter(Lecture.professor_id == Professor.id).all()
    return render_template('list.html')