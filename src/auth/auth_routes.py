from flask import Flask, request, render_template, redirect, flash, url_for
from flask_login import logout_user, login_user
from werkzeug.security import check_password_hash, generate_password_hash
from . import auth_bp
from src.models.user import User
from src.database.db import get_user_collection
from src.data.csu_campuses import CSU_CAMPUSES

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # check form 
        pass

    return render_template('login.html')

@auth_bp.route('/logout', methods=['GET'])
def logout():
    logout_user()
    flash('Successfully logged out!', category='success')
    return redirect(url_for('main.index'))

# create account
@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # check form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        college = request.form['college']
        coll = get_user_collection()

        user = {
            'first_name': first_name, 
            'last_name': last_name, 
            'email': email,
            'password': generate_password_hash(password, method='scrypt'),
            'college': college
        }
        
        doc = coll.find_one({"email": email})

        if doc: # email found in database
            flash('Email already exists!', category='error')
            return redirect(url_for('auth.login'))
        else: # email not found in db
            try:
                coll.insert_one(user)
                doc = coll.find_one({'email': email})
                flash('User created!', category='success')
                user = User(doc)
                login_user(user, remember=True)
                return redirect(url_for('main.index'))
            
            except Exception as e:
                pass

        return redirect(url_for('main.index'))

    return render_template('signup.html', csu_campuses=CSU_CAMPUSES)