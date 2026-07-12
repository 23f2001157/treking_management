from flask import Blueprint, request

auth = Blueprint("auth", __name__)

@auth.route("/register",methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Handle registration logic here
        return "Registration successful!"
    else:
        # Render registration form here
        return "Render registration form"