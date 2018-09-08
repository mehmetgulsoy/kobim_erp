import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Congfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'De haydi mehmet'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['m.mehmetgulsoy@gmail.com']
    LANGUAGES = ['tr', 'en']
    POSTS_PER_PAGE = os.environ.get('POSTS_PER_PAGE')
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
    FONT_AWESOME_CDN = os.environ.get('FONT_AWESOME_CDN')
    BOOTSTRAP_SERVE_LOCAL = True