from flask import Flask, render_template
app = Flask(__name__)
arduino='Arduino'
homen='Developers Space'
title=[]
@app.route("/")
def home():
	return render_template("Homepage.html", title=homen)
@app.route("/Arduino")
def ardpg():
	return render_template("Arduino.html", title=arduino)
