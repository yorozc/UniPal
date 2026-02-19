from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from bson import ObjectId
from . import pal_bp
from src.database.db import get_unipal_posts
from datetime import datetime

@pal_bp.route("/post/<post_id>", methods=['GET'])
def post(post_id):
    coll = get_unipal_posts()
    post = coll.find_one({"_id": ObjectId(post_id)})
    return render_template('pal_post.html', post=post)

@login_required
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
        curr_email = current_user.email
        curr_name = current_user.name
        
        coll = get_unipal_posts()

        date_obj = datetime.strptime(date, "%Y-%m-%d")
        formatted_date = date_obj.strftime("%m-%d-%Y")
        time_obj = datetime.strptime(time, "%H:%M")
        formatted_time = time_obj.strftime("%I:%M %p")

        post = {
            "name": curr_name,
            "email": curr_email,
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
@login_required
@pal_bp.route('/post/<post_id>/delete_post', methods=['POST'])
def delete_post(post_id):
    if request.method == 'POST':
        coll = get_unipal_posts()

        delete_result = coll.find_one_and_delete({"_id": ObjectId(post_id)})
        print(delete_result)

    return redirect(url_for('main.index'))

# editing a pal post

# reserving a slot on the pal post
