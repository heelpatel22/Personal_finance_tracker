import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'c30e4c90157ea0a015c48dca4194bead')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'instance/finance.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False