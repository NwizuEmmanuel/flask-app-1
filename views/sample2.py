from flask import Blueprint, render_template

sample2_bp = Blueprint('sample2_bp', __name__, template_folder="templates", static_folder="static", url_prefix="/sample2")

@sample2_bp.route("/")
def home():
    return render_template("sample2/sample2.html")