from flask import Flask, render_template, request, flash
from flask_login import current_user
from bson import ObjectId
from . import pal_bp
from src.database.db import get_unipal_posts
from datetime import datetime

# creating a pal post
@pal_bp.route('/add_post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        assn_name = request.form['work_name']
        desc = request.form['description']
        class_name = request.form['class']
        date = request.form['date']
        time = request.form['time']
        pals = request.form['amount']
        user_id = ObjectId(current_user.id)
        coll = get_unipal_posts()

        date_obj = datetime.strptime(date, "%Y-%m-%d")
        formatted_date = date_obj.strftime("%m-%d-%Y")
        time_obj = datetime.strptime(time, "%H:%M")
        formatted_time = time_obj.strftime("%I:%M %p")

        post = {
            "assignment": assn_name,
            "description": desc,
            "class": class_name,
            "start-date": date,
            "start-time": time,
            "pals": pals,
            "user_id": user_id
        }
        try:
            coll.insert_one(post)
            flash('Posted!', category='success')
        except Exception as e:
            flash(f'Error: {e}', category='error')

        print(assn_name, desc, class_name, formatted_date, formatted_time, pals, user_id)

    return render_template('pal_form.html')

# deleting a pal post

# editing a pal post

# reserving a slot on the pal post
