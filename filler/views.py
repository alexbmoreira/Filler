from flask import render_template
from filler import app

from .models import *

@app.route('/')
def index():
    game = Game()
    return render_template("home/index.html", game=str(game))
