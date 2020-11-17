from flask import render_template
from filler import app

@app.route('/')
def index():
    return render_template("home/index.html", word="WAZZZAAAPPP")
