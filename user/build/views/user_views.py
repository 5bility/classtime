from os import set_blocking
import re
from flask import Blueprint, render_template, url_for, request, session, flash, g
from werkzeug.security import check_password_hash
from werkzeug.utils import redirect

from build.app import db
from build.models import User

bp = Blueprint('user', __name__, url_prefix='/')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)

@bp.route('/signup', methods=('POST',))
def signup():
    id = request.form['id']
    pw = request.form['passwd']
    name = request.form['username']
    nickname = request.form['nickname']
    depart = request.form['depart']
    year = request.form['year']
    sex = request.form['sex']
    user = User(id=id, pw=pw, name=name, nickname=nickname, depart=depart, year=year, sex=sex)
    db.session.add(user)
    db.session.commit()
    
    logined = session.get('user_id')
    if logined is None:
        logined = 'false'
    return redirect('http://localhost:5001/home?login=' + str(logined))

@bp.route('/signin', methods=('POST',))
def signin():
    error = None
    id = request.form['id']
    pw = request.form['passwd']
    
    user = User.query.filter_by(id=id).first()
    
    if not user:
        error = "존재하지 않는 사용자입니다."
    elif user.pw != pw:
        error = "비밀번호가 올바르지 않습니다."
    if error is None:
        session.clear()
        session['user_id'] = user.id
        return redirect('http://localhost:5001/home?login=' + str(session.get('user_id')))
    flash(error)
    return redirect('http://localhost:5001/home?login=false')

@bp.route('/signout')
def signout():
    session.clear()
    return redirect('http://localhost:5001/home?login=false')