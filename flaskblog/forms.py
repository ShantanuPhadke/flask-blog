from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
	required_validator = DataRequired()
	
	username_length_validator = Length(min=2, max=20)
	username_validators = [required_validator, username_length_validator]
	username = StringField('Username', validators=username_validators)
	
	email_validator = Email()
	email_validators = [required_validator, email_validator]
	email = StringField('Email', validators=email_validators)

	password_validators = [required_validator]
	password = PasswordField('Password', validators=password_validators)

	confirm_password_validators = [required_validator, EqualTo('password')]
	confirm_password = PasswordField('Confirm Password', validators=confirm_password_validators)

	submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
	required_validator = DataRequired()

	email_validator = Email()
	email_validators = [required_validator, email_validator]
	email = StringField('Email', validators=email_validators)

	password_validators = [required_validator]
	password = PasswordField('Password', validators=password_validators)

	remember = BooleanField('Remember Me')

	submit = SubmitField('Login')

