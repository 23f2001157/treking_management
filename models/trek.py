from . import db


class Trek(db.Model):

    __tablename__ = "treks"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    location = db.Column(
        db.String(100),
        nullable=False
    )

    difficulty = db.Column(
        db.String(30),
        nullable=False
    )

    duration = db.Column(
        db.Integer,
        nullable=False
    )

    price = db.Column(
        db.Float,
        nullable=False
    )

    slots = db.Column(
        db.Integer,
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    bookings = db.relationship(
        "Booking",
        backref="trek",
        lazy=True
    )