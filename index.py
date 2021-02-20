from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")

def index():
    return render_template('index.html')

@app.route("/login")

def login():
    return render_template('login.hmtl')

@app.route("/profile")

def profile():
    return render_template('profile.html')


