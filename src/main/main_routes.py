from flask import Flask, redirect, url_for, render_template
from flask_login import current_user
from . import main_bp # blueprint
from src.database.db import get_unipal_posts, get_user_collection
from datetime import datetime


@main_bp.route('/')
def index():
    coll = get_unipal_posts()
    user_coll = get_user_collection()
    posts = list(coll.find({}))

    for post in posts:

        date_str = post.get('start-date')
        time_str = post.get('start-time')

        if date_str:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            post["start-date"] = date_obj.strftime("%b %d, %Y")

        if time_str:
            time_obj = datetime.strptime(time_str, "%H:%M")
            post["start-time"] = time_obj.strftime("%I:%M %p")

        post["_id"] = str(post["_id"])
        post["user_id"] = str(post.get("user_id", ""))
        pals_ids = post.get('pals_users', [])
        

        reserved_users = []
        if pals_ids:
            reserved_users = list(user_coll.find(
                {'_id': {'$in': pals_ids}},
                {'first_name': 1, 'last_name': 1, 'email': 1}
            ))

            for user in reserved_users:
                user["_id"] = str(user["_id"])
        
        pals_needed = post.get("pals", 0)
        reserved_count = len(post.get("pals_users", []))

        post["remaining"] = int(pals_needed) - reserved_count
    
    return render_template('index.html', posts=posts)