from flask import Flask, make_response, render_template, jsonify, request, session, redirect, url_for
from ..filler.models import Game, Color

app = Flask(__name__)

game = None

@app.route('/')
def index():
    global game
    game = Game()
    return render_template("home/index.html", game=game.toDict())

@app.route('/make-move')
def make_move():
    global game
    color = Color(request.args["color"])
    game.player_1.makeMove(game.board, color)

    return render_template("home/game.html", game=game.toDict())

@app.route('/ai-make-move')
def ai_make_move():
    global game
    game.computer.aiMakeMove(game.board)

    return render_template("home/game.html", game=game.toDict())