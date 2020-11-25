from flask import make_response, render_template, jsonify, request, session, redirect, url_for
from . import app

from ..filler.models import Game

@app.route('/')
def index():
    game = Game().toJSON()
    return render_template("home/index.html", game=game)
