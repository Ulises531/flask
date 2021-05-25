from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def url_principal():
	return render_template("template.html",nombre="Ulises Barroso")

@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/navbar")
def navbar():
	return render_template("navbar.html")

@app.route("/styles1")
def styles1():
	return render_template("styles1.css")


if __name__ == "__main__":
	app.run(debug=True)
