from flask import Flask, request, render_template, redirect, flash, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from . import auth_bp
from database.db import get_user_collection
from src.data.csu_campuses import CSU_CAMPUSES

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # check form 
        pass

    return render_template('login.html')

# create account
@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # check form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        major = request.form['major']
        college = request.form['college']

        user = {
            'first_name': first_name, 
            'last_name': last_name, 
            'email': email,
            'password': generate_password_hash(password, method='scrypt'),
            'major': major,
            'college': college
        }
        
        coll = get_user_collection()
        
        # search for existing email
        # if email is found show that it already exists
        # if not found, add to db
        return redirect(url_for('main.index'))

    return render_template('signup.html', csu_campuses=CSU_CAMPUSES)