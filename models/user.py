from datetime import datetime
from models import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password_hash = db.Column(db.String(255), nullable=False)

    phone = db.Column(db.String(15))

    role = db.Column(db.String(20), nullable=False)

    is_approved = db.Column(db.Boolean, default=True)

    is_blacklisted = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


    assigned_treks = db.relationship(
        "Trek",
        backref="assigned_staff",
        lazy=True
    )

    bookings = db.relationship(
        "Booking",
        backref="user",
        lazy=True
    )

    def __repr__(self):
        return f"<User {self.name}>"