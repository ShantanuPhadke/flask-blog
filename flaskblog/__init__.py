from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
# Importing in the bcrypt module
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager

# Application and Database Configuration below here
app = Flask(__name__)
app.config['SECRET_KEY'] = '8479fd7bef4ebf6c264fd36063af37b8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
# Making a bcrypt object for the app
bcrypt = Bcrypt(app)
# Making a LoginManager object for the app
login_manager = LoginManager(app)
login_manager.login_view = 'login' # default view to show when login_required is not met
login_manager.login_message_category = 'info' # Formatting the message that is shown

# Application and Database Configuration above here

from flaskblog import routes