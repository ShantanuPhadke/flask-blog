from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
# Since both the forms and models are now inside the flaskblog folder, we use
# these are what the new imports would look like.
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

# Dummy post data, valuable because it tells us the proper
# schema for individual Post Objects
posts = [
	{
		'author': 'Corey Schafer',
		'title': 'Blog Post 1',
		'content': 'First Post Content!',
		'date_posted': 'August 17, 2019'
	},

	{
		'author': 'Jane Doe',
		'title': 'Blog Post 2',
		'content': 'Second Post Content!',
		'date_posted': 'August 18, 2019'
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
	# Checks if the current user is already authenticated,because in this
	# case we do not want them to be able to access the Register page!
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	registration_form = RegistrationForm()
	if registration_form.validate_on_submit():
		# Hashing the user entered password
		hashed_password = bcrypt.generate_password_hash(registration_form.password.data).decode('utf-8')
		# Making new User with entered username email and password and committing the change
		user = User(username=registration_form.username.data, email=registration_form.email.data, password=hashed_password)
		db.session.add(user) # Adding the new user to the database
		db.session.commit() # Commiting all of our previous changes, in this case only the one
		flash(f'Your account has been created! You can now log in!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=registration_form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	# Checks if the current user is already authenticated,because in this
	# case we do not want them to be able to access the Login page!
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	login_form = LoginForm()
	# SAMPLE VALIDATION BELOW
	if login_form.validate_on_submit():
		user = User.query.filter_by(email=login_form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, login_form.password.data):
			login_user(user, remember=login_form.remember.data)
			# The next parameter carries the name of the endpoint the user was originally
			# trying to access, so we will redirect them to that endpoint after logging in!
			# Otherwise, if there is no next page we redirect to the home route.
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home')) 
		else:
			flash('Login Unsuccessful. Please check email and password', 'danger')
	# SAMPLE VALIDATION ABOVE
	return render_template('login.html', title='Login', form=login_form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))

# For the account endpoint we utilize the login_required decorator
# in order to make sure that the user is already authenticated when
# accessing the account page! If an user who isn't logged in tries to
# access the Account page, they will be redirected to the Login form!
@app.route("/account")
@login_required
def account():
	return render_template('account.html', title="Account")
