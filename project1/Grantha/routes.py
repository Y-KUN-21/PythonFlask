from flask import render_template, url_for, redirect, flash
from Grantha import app,db,bcrypt
from Grantha.form import signupForm, loginForm
from Grantha.models import User


@app.route('/')
def home():
    return render_template("Home.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email_id.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            flash("Logged in Successfully", 'success')
            return redirect(url_for('home'))
        else:
            flash("Please check Your Email or Password.", 'danger')
    return render_template("login.html", title="Login", form=form)


@app.route('/signup', methods=['POST', 'GET'])
def register():
    form = signupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        adduser = User(username=form.username.data, email=form.email_id.data, password=hashed_password)
        db.session.add(adduser)
        db.session.commit()
        flash("Account created.", 'success')
        return redirect(url_for('login'))
    return render_template("signup.html", title="SignUp", form=form)
