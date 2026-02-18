from flask import Flask
from . import user_bp

@user_bp.route('/user_profile/<user_id>', methods=['GET', 'POST'])
def user_profile(user_id):
    # return user with current user id through path parameter
    return 'user'
