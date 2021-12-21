# SQLAlchemy 모델 기반 데이터베이스 처리
from sqlalchemy.orm import backref
from app import db

class User(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    pw = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    nickname = db.Column(db.String(20), nullable=False)
    depart = db.Column(db.String(20), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(3), nullable=False)
    
class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    depart = db.Column(db.String(20), nullable=False)

class Lecture(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    classroom = db.Column(db.String(20), nullable=False)
    classtime = db.Column(db.String(50), nullable=False)
    student_count = db.Column(db.Integer, nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    professor = db.relationship('Professor', backref=db.backref('lectuer_set'))
    
class Evaluation(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    comment = db.Column(db.Text(), nullable=False)
    stars = db.Column(db.Integer(), nullable=False)
    user_id =  db.Column(db.String(20), db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('eval_set'))
    lecture_id = db.Column(db.Integer, db.ForeignKey('lecture.id', ondelete='CASCADE'), nullable=False)
    lecture = db.relationship('Lecture', backref=db.backref('eval_set', cascade='all, delete-orphan'))

class Grade(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    grade = db.Column(db.String(5), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    semester = db.Column(db.Integer(), nullable=False)
    user_id = db.Column(db.String(20), db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('grade_set', cascade='all, delete-orphan'))
    lecture_id = db.Column(db.Integer(), db.ForeignKey('lecture.id'), nullable=False)
    lecture = db.relationship('Lecture', backref=db.backref('grade_set'))

class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    posttime = db.Column(db.DateTime(), nullable=False)
    recommends = db.Column(db.Integer(), nullable=False)
    replys = db.Column(db.Integer(), nullable=False)
    user_id = db.Column(db.String(20), db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('post_set'))
    
class Recommend(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(20), db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('recommend_set'))
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id'), nullable=False)
    post = db.relationship('Post', backref=db.backref('recommend_set'))
    
class Reply(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    replytime = db.Column(db.DateTime(), nullable=False)
    comment = db.Column(db.Text(), nullable=False)
    is_added = db.Column(db.Integer(), nullable=False)
    added_id = db.Column(db.Integer(), nullable=False)
    user_id = db.Column(db.String(20), db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('reply_set'))
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id'), nullable=False)
    post = db.relationship('Post', backref=db.backref('reply_set'))