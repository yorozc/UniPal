from flask import Flask
from . import pal_bp

@pal_bp.route('/pal_posts')
def pal_posts():
    pass