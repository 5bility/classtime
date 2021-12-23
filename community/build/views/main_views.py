from flask import Blueprint, render_template

from build.models import Post, User
from build.app import db

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return 'Hello, Pybo'

@bp.route('/community')
def community():
    post_list = db.session.query(Post.id, Post.title, User.name, Post.posttime, Post.recommends, Post.replys).filter(Post.user_id == User.id).all()
    return render_template('community.html', post_list=post_list)

@bp.route('/post')
def post():
    return render_template('post.html')