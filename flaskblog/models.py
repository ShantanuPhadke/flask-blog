from flaskblog import db, login_manager
from datetime import datetime 
from flask_login import UserMixin 

# Helper function that takes in an user id as input
# and returns the corresponding User object. It is 
# needed for the Flask's LoginManager needs to work
# properly.
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
 
# Defining the Schema for the User Database Model
class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	# The following posts column will be a backref which allows SQLAlchemy to link 
	# a specific user (author) back to a bunch of different posts they wrote
	posts = db.relationship('Post', backref='author', lazy=True)

	# Defines the default manner in which our object will be printed out
	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# Defining the Schema for the Post Database Model
class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	# user_id = id for the user who made this specific post
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


	# Defines the default manner in which our object will be printed out
	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"

