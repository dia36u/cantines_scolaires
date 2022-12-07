"""Routes for parent Flask app."""
from flask import current_app as app
from flask import render_template

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/page1")
def page1():
    return render_template('page1.html')

@app.route("/page2")
def page2():
    return render_template('page2.html')

@app.route("/page3")
def page3():
    return render_template('page3.html')