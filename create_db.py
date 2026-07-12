import os

from flask import Flask

from config import Config
from models import db

# Import all models so SQLAlchemy knows about them
from models.user import User
from models.trek import Trek
from models.booking import Booking
from models.payment import Payment


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


if __name__ == "__main__":
    os.makedirs("database", exist_ok=True)

    with app.app_context():
        db.create_all()

    print("Database created successfully!")