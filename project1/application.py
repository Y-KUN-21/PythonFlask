from flask import Flask, render_template, url_for, redirect,flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from form import signupForm,loginForm
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'PFzS9qWgQqTUv6BQjQlmJg'

@app.route('/')
def home():
    return render_template("Home.html")


@app.route('/login', methods=['POST','GET'])
def loginpage():
    form = loginForm()
    return render_template("login.html",title="Login",form=form)


@app.route('/signup', methods=['POST','GET'])
def register():
    form = signupForm()
    if form.validate_on_submit():
        flash("Account created.",'danger')
        return redirect(url_for('home'))
    return render_template("signup.html", title="SignUp", form=form)

if __name__ == "__main__":
    app.run(debug=True)
