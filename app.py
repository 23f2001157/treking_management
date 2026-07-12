from flask import Flask, render_template
from routes.auth import auth
# from routes.admin import admin
# from routes.staff import staff
# from routes.user import user
from config import Config
from models import db

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(auth)
# app.register_blueprint(admin)
# app.register_blueprint(staff)
# app.register_blueprint(user)


@app.route("/")
def homePage():
    return render_template("homePage.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)