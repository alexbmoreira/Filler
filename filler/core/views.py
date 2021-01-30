from flask import Flask, make_response, render_template, jsonify, request, session, redirect, url_for
from ..filler.models import Game, Color
import json

app = Flask(__name__)

@app.route('/')
def index():
    game = Game()
    return render_template("home/index.html", game=game.toDict(), json=json.dumps(game.toDict()))

@app.route('/make-move', methods=["POST"])
def make_move():
    data = request.get_json()

    color = Color(data["color"])
    game = Game.fromDict(data["game"])

    game.player_1.makeMove(game.board, color)

    return render_template("home/game.html", game=game.toDict(), json=json.dumps(game.toDict()))

@app.route('/ai-make-move', methods=["POST"])
def ai_make_move():
    data = request.get_json()

    game = Game.fromDict(data["game"])
    game.computer.aiMakeMove(game.board)

    return render_template("home/game.html", game=game.toDict(), json=json.dumps(game.toDict()))