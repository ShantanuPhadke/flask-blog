from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


# Application and Database Configuration below here
app = Flask(__name__)
app.config['SECRET_KEY'] = '8479fd7bef4ebf6c264fd36063af37b8'
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
# Application and Database Configuration above here

from flaskblog import routes