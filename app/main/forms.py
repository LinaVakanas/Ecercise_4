from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, Form, SelectField
from wtforms.validators import DataRequired, EqualTo, Email


class SignupForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    name = StringField("What's your name?")
    email = StringField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')


class CityBlogSearchForm(Form):
    choices = [('City', 'City'),
               ('Blog', 'Blog')]
    select = SelectField('', choices=choices)
    search = StringField('Search blog or city...', validators=[DataRequired()])


