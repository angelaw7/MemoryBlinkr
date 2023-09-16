from flask import Flask, jsonify, request, send_from_directory
from flask import jsonify
import gridgame

from blink_detector.BlinkDetector import BlinkDetector

global old_grid
blink_detector = BlinkDetector()

app = Flask(__name__)


@app.route("/")
def hello_world():
    return send_from_directory("templates/", 'index.html')  

@app.route('/get-grid', methods=['POST'])
def sendGridGame():
    global old_grid
    grid_size = request.json['grid_size']
    old_grid = gridgame.generateGrid(grid_size, grid_size)
    return jsonify(old_grid)


@app.route("/await-blink", methods=["GET"])
def awaitBlink():
    """
    Wait for the blink response
    """
    blink_detector.start()
    return {"response": 200}


@app.route("/compare-grids", methods=["POST"])
def compareGrids():
    """
    Compare the originally generated grid with the user submitted grid
    """
    new_grid = request.get_json()
    return jsonify(gridgame.compareGrid(old_grid, new_grid))
