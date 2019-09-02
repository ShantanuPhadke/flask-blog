# Now running our app is the ONLY function for this file!
from flaskblog import app

if __name__ == '__main__':
	app.run(debug=True)