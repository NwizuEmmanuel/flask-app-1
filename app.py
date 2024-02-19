from flask import Flask
from views import sample1, sample2

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(sample1.sample1_bp)
app.register_blueprint(sample2.sample2_bp)

if __name__ == "__main__":
    app.run()