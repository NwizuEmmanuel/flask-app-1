from flask import Blueprint, render_template

sample1_bp = Blueprint('sample1_bp', __name__, template_folder="templates", static_folder="static")

@sample1_bp.route("/1")
def home():
    return render_template("sample1/sample1.html")