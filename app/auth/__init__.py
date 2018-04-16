# app/catalog/__init__

from flask import Blueprint
authentication = Blueprint('authentication', __name__, template_folder='templates')


# import at the bottom to avoid cross-reference issues
from app.auth import routes
