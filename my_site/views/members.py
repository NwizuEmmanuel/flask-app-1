from flask import Blueprint, render_template
from my_site.models import ClassMembers
from my_site.database import db

members = Blueprint('members', __name__, template_folder="templates", static_folder="static")

@members.route("/")
def list_member():
    class_members = db.session.execute(db.select(ClassMembers).order_by(ClassMembers.firstname)).scalars()
    return render_template("member/list.html", class_members=class_members)