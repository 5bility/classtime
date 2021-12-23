from flask import Blueprint, render_template, request, session, redirect
from flask.helpers import url_for

from build.models import Post, User
from build.app import db

from datetime import date, datetime

bp = Blueprint('post', __name__, url_prefix='/')

@bp.route('/post', methods=('POST',))
def post():
    title = request.form['title']
    content = request.form['content']
    
    post = Post(title=title, content=content, posttime=datetime.now(), recommends=0, replys=0, user_id='rt3310')
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('main.community'))