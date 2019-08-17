from flask import Flask , render_template
app = Flask(__name__)

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
def hello():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', title="About")

if __name__ == '__main__':
	app.run(debug=True)