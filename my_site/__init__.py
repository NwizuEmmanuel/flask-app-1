from flask import Flask
from .views import sample1, sample2
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)

app.config.from_pyfile('config.py')
db = SQLAlchemy()
db.init_app(app)
toolbar = DebugToolbarExtension(app)
app.register_blueprint(sample1.sample1_bp)
app.register_blueprint(sample2.sample2_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()