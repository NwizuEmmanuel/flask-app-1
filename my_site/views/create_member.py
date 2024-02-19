from flask import Blueprint, render_template, redirect, request, url_for
from ..models import ClassMembers
from .. import db

create_member_bp = Blueprint("create_member_bp", __name__, template_folder="templates", static_folder="static")

@create_member_bp.route("/create", method=["POST"])
def create():
    if request.method == "POST":
        fname = request.form["firstname"]
        mname = request.form["middlename"]
        lname = request.form["lastname"]
        member = ClassMembers(
            firstname = fname,
            middlename = mname,
            lastname = lname
        )
        db.session.add(member)
        db.session.commit()
        return redirect(url_for("list_member"))
    else:
        render_template("member/create.html")