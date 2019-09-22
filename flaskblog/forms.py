from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

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

	# A function to check that the entered username is unique BEFORE we try to
	# add it into our database
	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is taken. Please choose a different one.')

	# A function to check that the entered email is unique BEFORE we try to add
	# it into our database
	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
	required_validator = DataRequired()

	email_validator = Email()
	email_validators = [required_validator, email_validator]
	email = StringField('Email', validators=email_validators)

	password_validators = [required_validator]
	password = PasswordField('Password', validators=password_validators)

	remember = BooleanField('Remember Me', default='checked', validators=[required_validator])

	submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
	required_validator = DataRequired()
	
	username_length_validator = Length(min=2, max=20)
	username_validators = [required_validator, username_length_validator]
	username = StringField('Username', validators=username_validators)
	
	email_validator = Email()
	email_validators = [required_validator, email_validator]
	email = StringField('Email', validators=email_validators)

	picture_files_allowed_validator = [FileAllowed(['jpg', 'png'])]
	picture = FileField('Update Profile Picture', validators=picture_files_allowed_validator)

	submit = SubmitField('Update')

	# A function to check that the entered username is unique BEFORE we try to
	# add it into our database
	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('That username is taken. Please choose a different one.')

	# A function to check that the entered email is unique BEFORE we try to add
	# it into our database
	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('That email is taken. Please choose a different one.')


