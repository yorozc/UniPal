from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from bson import ObjectId
from . import pal_bp
from src.database.db import get_unipal_posts, get_user_collection
from datetime import datetime

@pal_bp.route("/post/<post_id>", methods=['GET'])
def post(post_id):
    coll = get_unipal_posts()
    user_coll = get_user_collection()
    post = coll.find_one({"_id": ObjectId(post_id)})

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
    

    return render_template('pal_post.html', post=post, reserved_users=reserved_users)

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

        post = {
            "name": curr_name,
            "email": curr_email,
            "assignment": assn_name,
            "description": desc,
            "class": class_name,
            "start-date": date,
            "start-time": time,
            "pals": pals,
            "user_id": user_id,
            "pals_users": []
        }
        try:
            coll.insert_one(post)
            flash('Posted!', category='success')
        except Exception as e:
            flash(f'Error: {e}', category='error')

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
@login_required
@pal_bp.route('/post/<post_id>/edit_post', methods=['GET', 'POST'])
def edit_post(post_id):
    coll = get_unipal_posts()
    if request.method == 'POST':
        upd_assignment = request.form['assignment']
        upd_desc = request.form['description']
        upd_class = request.form['class']
        upd_date = request.form['date']
        upd_time = request.form['time']
        upd_pals = request.form['pals']
        
        data = {
            "assignment": upd_assignment,
            "description": upd_desc,
            "class": upd_class,
            "start-date": upd_date,
            "start-time": upd_time,
            "pals": upd_pals
        }

        coll.update_one(
            {"_id": ObjectId(post_id)},
            {"$set": data}
        )
        return redirect(url_for('main.index'))
        
        
    post = coll.find_one({"_id": ObjectId(post_id)})
    assignment = post['assignment']
    desc = post['description']
    class_name = post['class']
    date = post['start-date']
    time = post['start-time']
    pals = post['pals']
    return render_template('pal_edit_post.html', assignment=assignment, desc=desc, class_name=class_name, 
                           date=date, time=time, pals=pals, post=post)

# reserving a slot on the pal post
@pal_bp.route('/post/<post_id>/reserve', methods=['POST'])
@login_required
def reserve(post_id):
    coll = get_unipal_posts()

    reserve_check = coll.update_one(
        {"_id": ObjectId(post_id)},
        {"$addToSet": {"pals_users": ObjectId(current_user.id)}}
    )
    if reserve_check.modified_count == 0:
        flash('You already reserved a slot.', category='error')
    elif reserve_check.matched_count == 0:
        flash('Post not found.', category='error')
    else:
        flash("Reserved!", category='success')

    return redirect(url_for('pal.post', post_id=post_id))

@pal_bp.route('/post/<post_id>/unreserve', methods=['POST'])
@login_required
def unreserve(post_id):
    coll = get_unipal_posts()

    result = coll.update_one(
        {"_id": ObjectId(post_id)},
        {"$pull": {"pals_users": ObjectId(current_user.id)}}
    )

    if result.matched_count == 0:
        flash("Post not found.", "error")
    elif result.modified_count == 0:
        flash("You were not reserved for this post.", "info")
    else:
        flash("Reservation cancelled.", "success")

    return redirect(url_for('pal.post', post_id=post_id))
