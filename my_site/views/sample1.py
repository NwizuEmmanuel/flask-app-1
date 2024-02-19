from flask import Blueprint, render_template

sample1_bp = Blueprint('sample1_bp', __name__, template_folder="templates", static_folder="static", url_prefix="/sample1")

@sample1_bp.route("/")
def home():
    return render_template("sample1/sample1.html")