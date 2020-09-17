from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
	return render_template("Homepage.html")
@app.route("/Arduino")
def ardpg():
	return render_template("Arduino.html")
