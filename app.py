from flask import Flask, render_template
from flask_login import LoginManager, current_user

from config import Config
from models import db
from models.user import User

# Import models so SQLAlchemy registers them
from models.trek import Trek
from models.booking import Booking
from models.payment import Payment

# Import blueprints
from routes.auth import auth

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


app.register_blueprint(auth)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    if current_user.is_authenticated:
        return render_template("dashboard.html")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)