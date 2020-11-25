from flask import render_template
from . import app

from ..filler.models import Game

@app.route('/')
def index():
    game = Game()
    return render_template("home/index.html", game=str(game))
