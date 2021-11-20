from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/bookings')
def bookings():
    return render_template("bookings.html")

@auth.route('/history')
def history():
    return render_template("history.html")

@auth.route('/gallery')
def sign_up():
    return render_template("gallery.html")

@auth.route('/home')
def home():
    return render_template("home.html")
