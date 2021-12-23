# 초기 시작 파일
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import sys
sys.path.append('.')
import config


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config) # app.config 환경 변수 설정
    
    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from build import models
    
    # blueprint
    from build.views import main_views, post_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(post_views.bp)
    
    return app