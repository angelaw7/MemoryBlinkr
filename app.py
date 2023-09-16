from flask import Flask, jsonify, request
import gridgame

from blink_detector.BlinkDetector import BlinkDetector

global old_grid
blink_detector = BlinkDetector()

app = Flask(__name__)


@app.route("/")
def health_check():
    return "<p>healthy!</p>"


@app.route("/get-grid", methods=["GET"])
def getGrid():
    """
    Get a randomly generated grid
    """
    global old_grid
    old_grid = gridgame.generateGrid(5, 5)
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
