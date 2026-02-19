from flask import Blueprint

pal_bp = Blueprint('pal', __name__)

from . import pal_routes