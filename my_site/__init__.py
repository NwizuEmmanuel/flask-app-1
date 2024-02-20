from flask import Flask
from my_site.views import sample1, sample2, members, create_member
from flask_sqlalchemy import SQLAlchemy
from my_site.database import db

def main_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    app.register_blueprint(sample1.sample1_bp, url_prefix="/sample")
    app.register_blueprint(sample2.sample2_bp, url_prefix="/sample")
    app.register_blueprint(create_member.create_member_bp, url_prefix="/member")
    app.register_blueprint(members.members, url_prefix="/member")

    return app