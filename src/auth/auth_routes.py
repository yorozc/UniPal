from flask import Flask
from . import auth_bp

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return 'login'

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    return 'signup'