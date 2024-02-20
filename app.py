from my_site import main_app
from my_site.database import db

if __name__ == "__main__":
        with main_app().app_context():
            db.create_all()
        main_app().run()