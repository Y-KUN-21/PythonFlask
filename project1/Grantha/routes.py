from flask import render_template, url_for, redirect, flash
from flask_bootstrap import Bootstrap
from Grantha import app
from Grantha import db
from Grantha import bcrypt
from Grantha.form import signupForm, loginForm
from Grantha.models import User


@app.route('/')
def home():
    return render_template("Home.html")


@app.route('/login', methods=['POST', 'GET'])
def loginpage():
    form = loginForm()
    return render_template("login.html", title="Login", form=form)


@app.route('/signup', methods=['POST', 'GET'])
def register():
    form = signupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        adduser = User(username=form.username.data, email=form.email_id.data, password=hashed_password)
        db.session.add(adduser)
        db.session.commit()
        flash("Account created.", 'danger')
        return redirect(url_for('loginpage'))
    return render_template("signup.html", title="SignUp", form=form)
