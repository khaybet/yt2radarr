from flask import Blueprint, render_template, request
main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    ...
