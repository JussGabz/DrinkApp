from flask_login import UserMixin
from app import db


class Users(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
