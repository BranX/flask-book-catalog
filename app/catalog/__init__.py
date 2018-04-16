# app/catalog/__init__

from flask import Blueprint
main = Blueprint('main', __name__, template_folder='templates')


# import at the bottom to avoind cross-reference issues
from app.catalog import routes
