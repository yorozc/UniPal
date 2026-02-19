from flask import Flask, request, render_template, redirect, flash
from . import auth_bp
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
    if request.method == "POST":
        # check form data
        
        # get users collection
        # search for existing email
        # if email is found show that it already exists
        # if not found, add to db
        pass

    return render_template('signup.html', csu_campuses=CSU_CAMPUSES)