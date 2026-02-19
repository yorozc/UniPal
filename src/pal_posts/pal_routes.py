from flask import Flask, render_template, request
from . import pal_bp
from src.database.db import get_user_collection
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

        date_obj = datetime.strptime(date, "%Y-%m-%d")
        formatted_date = date_obj.strftime("%m-%d-%Y")

        print(assn_name, desc, class_name, formatted_date, time, pals)

    return render_template('pal_form.html')

# deleting a pal post

# editing a pal post

# reserving a slot on the pal post
