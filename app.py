from flask import Flask
import gridgame
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/start-gridgame', methods=['POST'])
def sendGridGame():
    return jsonify(gridgame.generateGrid(arr))

@app.route('/receive-player-grid', methods=['POST'])
def receiveGridGame():
    return jsonify(gridgame.compareGrid(arr))

