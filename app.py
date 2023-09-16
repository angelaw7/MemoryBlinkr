from flask import Flask, request, render_template
from flask import jsonify
import gridgame
import json

app = Flask(__name__)

global old_grid

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/start-gridgame', methods=['POST'])
def sendGridGame():
    global old_grid
    old_grid = gridgame.generateGrid(5, 5)
    return jsonify(old_grid)

@app.route('/receive-player-grid', methods=['POST'])
def receiveGridGame():
    new_grid = request.get_json()
    return jsonify(gridgame.compareGrid(old_grid, new_grid))

