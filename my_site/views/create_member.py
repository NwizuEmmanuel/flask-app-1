from flask import Blueprint, render_template, redirect, request, url_for
from my_site.models import ClassMembers
from my_site.database import db

create_member_bp = Blueprint("create_member_bp", __name__, template_folder="templates", static_folder="static")

@create_member_bp.route("/create", methods=["POST", "GET"])
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
        return redirect(url_for("members.list_member"))
    return render_template("member/create.html")