from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.auth.models import User


def email_exist(form, field):
    email = User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError('Email Already Exists!')


class RegistrationForm(FlaskForm):
    name = StringField("What's your Name", validators=[DataRequired(), Length(3, 15, message='between 3 to 15 characters')])
    email = StringField('Enter your Email', validators=[DataRequired(), Email(), email_exist])
    password = PasswordField('Password', validators=[DataRequired(), Length(5), EqualTo('confirm', message='passwords must match')])
    confirm = PasswordField('Confirm', validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_loggedin = BooleanField('stay logged-in')  # checkbox
    submit = SubmitField('LogIn')
