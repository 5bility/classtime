from flask import Blueprint, render_template, redirect
from flask.helpers import url_for
from build.models import Grade

bp = Blueprint('addgrade', __name__, url_prefix='/')

@bp.route('/addgrade', methods=('POST',))
def addgrade():
    return redirect(url_for('main.grade'))