from flask import Flask, render_template

#Create a Flask Instance


app = Flask(__name__)


#Create a route decorator

@app.route("/")

def index():

	favorite_pizza = ["ananas", "salami", "quattro stagionni"]
	return render_template("index.html", favorite_pizza = favorite_pizza)

@app.route("/user/<name>")
def user(name):
	return render_template("user.html", user_name = name)


#invalid URL

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404



@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500
