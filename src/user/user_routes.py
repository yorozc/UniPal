from flask import Flask
from . import user_bp

@user_bp.route('/user_profile', methods=['GET', 'POST'])
def user_profile():
    return 'user'
