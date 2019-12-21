from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length,Email,Required

class signupForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email_id = StringField('Email-Address',validators=[DataRequired(),Email()])
    password =PasswordField('Password',validators=[DataRequired(),Length(min=8)])
    submit = SubmitField('Sign up')


class loginForm(FlaskForm):
    email_id = StringField('Email-Address',validators=[DataRequired(),Email()])
    password =PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
