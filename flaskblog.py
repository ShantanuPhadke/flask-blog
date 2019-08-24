from flask import Flask , render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '8479fd7bef4ebf6c264fd36063af37b8'

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
	registration_form = RegistrationForm()
	if registration_form.validate_on_submit():
		flash(f'Account created for {registration_form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=registration_form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	login_form = LoginForm()
	# SAMPLE VALIDATION BELOW
	if login_form.validate_on_submit():
		if login_form.email.data == 'admin@blog.com' and login_form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check username and password', 'danger')
	# SAMPLE VALIDATION ABOVE
	return render_template('login.html', title='Login', form=login_form)


if __name__ == '__main__':
	app.run(debug=True)