# 프로젝트 환경 설정
import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'mysql://classtimepm:ct1234@ct_mysql/classtime?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False