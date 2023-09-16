from flask import Flask, jsonify, request, send_from_directory
import gridgame
# import paragraphGame
from blink_detector.BlinkDetector import BlinkDetector

global old_grid, old_paragraph
blink_detector = BlinkDetector()

app = Flask(__name__)


@app.route("/")
def health_check():
    return send_from_directory("templates/", "index.html")


@app.route("/get-grid", methods=["POST"])
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


@app.route("/get-paragraph", methods=["POST"])
def getParagraph():
    global old_paragraph
    old_paragraph = paragraphGame.generateParagraph(50)
    return jsonify(old_paragraph)


@app.route("/compare-paragraphs", methods=["POST"])
def compareParagraphs():
    new_paragraph = request.get_json()
    paragraphGame.compareParagraph(old_paragraph, new_paragraph)


