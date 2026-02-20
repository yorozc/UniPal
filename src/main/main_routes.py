from flask import Flask, redirect, url_for, render_template
from flask_login import current_user
from . import main_bp # blueprint
from src.database.db import get_unipal_posts
from datetime import datetime


@main_bp.route('/')
def index():
    coll = get_unipal_posts()
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
    
    return render_template('index.html', posts=posts)