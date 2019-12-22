from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from flask_bcrypt import Bcrypt


app = Flask(__name__)
Bootstrap(app)
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = 'PFzS9qWgQqTUv6BQjQlmJg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
db = SQLAlchemy(app)

from Grantha import routes