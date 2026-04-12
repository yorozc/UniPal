from flask import Flask
from . import user_bp

@user_bp.route('/user/<user_id>/profile', methods=['GET'])
def user_profile(user_id):
    # return user with current user id through path parameter
    # path: /user_profile/187393 (show that user's profile)
    return 'user'
