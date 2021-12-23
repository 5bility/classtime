from os import set_blocking
import re
from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return 'Hello, Pybo'

@bp.route('/signup')
def signup():
    return render_template('signup.html')

@bp.route('/signin')
def signin():
    return render_template('signin.html')