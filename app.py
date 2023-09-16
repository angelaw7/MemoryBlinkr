from flask import Flask, jsonify, request, send_from_directory, redirect
import gridgame

import wordsGame
from blink_detector.BlinkDetector import BlinkDetector

global old_grid, old_paragraph
blink_detector = BlinkDetector()

app = Flask(__name__)
blink_detector.activate_cam()


@app.route("/")
def health_check():
    return send_from_directory("templates/", "menu.html")


@app.route("/grid-game")
def loadGridPage():
    return send_from_directory("templates/", "index.html")


@app.route("/image-game")
def loadImagePage():
    return send_from_directory("templates/", "canvas.html")


@app.route("/phrase-game")
def loadPhrasePage():
    return send_from_directory("templates/", "phrases.html")


@app.route("/get-grid", methods=["POST"])
def getGrid():
    """
    Get a randomly generated grid
    """
    global old_grid
    grid_size = request.json["grid_size"]
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
    data = request.get_json()
    return jsonify(gridgame.compareGrid(data["oldGrid"], data["newGrid"]))


@app.route("/get-phrase", methods=["POST"])
def getPhrase():
    topic = request.get_json()["topic"]
    original_phrases = wordsGame.generatePhrase(topic)
    return jsonify(original_phrases)


@app.route("/compare-phrases", methods=["POST"])
def comparePhrases():
    data = request.get_json()
    orig_phrase = data["original_phrases"]
    user_phrase = data["user_phrases"]
    score = wordsGame.comparePhrases(orig_phrase, user_phrase)

    return {"score": score / (max(len(orig_phrase), len(user_phrase)))}
