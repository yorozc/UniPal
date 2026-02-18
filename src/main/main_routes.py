from flask import Flask
from . import main_bp # blueprint


@main_bp.route('/')
def index():
    return 'Should work'