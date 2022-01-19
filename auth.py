from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from models import Users
from app import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template("login.html")


@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = Users.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check log in details and try again')
        # If user does not exist or pass is wrong, redirect to login page
        return redirect(url_for('auth.login'))
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    return render_template("signup.html")


@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user user to database goes here
    username = request.form.get('username')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')

    user = Users.query.filter_by(username=username).first()

    # If User exists redirect back to signup page so user can try again
    if user:
        flash('Username already exists')
        return redirect(url_for('auth.signup'))

    # Create new user with information from form data. Hash the Password also
    # so it is not stored in plaintext
    new_user = Users(
        username=username,
        fname=fname,
        lname=lname,
        email=email,
        password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
