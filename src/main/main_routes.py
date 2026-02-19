from flask import Flask, redirect, url_for, render_template
from . import main_bp # blueprint
from src.database.db import get_unipal_posts


@main_bp.route('/')
def index():
    coll = get_unipal_posts()

    return render_template('index.html', posts=coll.find({}))