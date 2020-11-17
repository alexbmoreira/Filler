from flask import Flask, make_response, render_template, jsonify, request, session, redirect, url_for

app = Flask(__name__, template_folder='filler/templates', static_folder='filler/static')

@app.route('/')
def index():
    return render_template('home/index.html')