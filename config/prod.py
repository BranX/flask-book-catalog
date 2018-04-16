import os

DEBUG = False
SECRET_KEY = 'topsecret'
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Supersonic1981@localhost/catalog_db'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False

