from flask import Flask, redirect, url_for, render_template
from . import main_bp # blueprint


@main_bp.route('/')
def index():
    return render_template('index.html')