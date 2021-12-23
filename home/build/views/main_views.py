import re
from flask import Blueprint, render_template, request, session
from werkzeug.utils import redirect
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo'

@bp.route('/home')
def home():
    # logined = request.args.get('login')
    
    # if logined != 'false':
    #     session['user_id'] = logined
    return render_template('home.html')

@bp.route('/signin')
def signin():
    return redirect('http://localhost:5002/signin')

@bp.route('/signup')
def signup():
    return redirect('http://localhost:5002/signup')