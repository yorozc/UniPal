from flask import Flask, request, render_template, redirect, flash
from . import auth_bp

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        pass

    return render_template('login.html')

# create account
@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        pass

    return render_template('signup.html')