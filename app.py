from flask import Flask, jsonify, request, send_from_directory
import gridgame

app = Flask(__name__)

global old_grid

@app.route("/")
def hello_world():
    return send_from_directory("templates/", 'index.html')  

@app.route('/get-grid', methods=['POST'])
def sendGridGame():
    global old_grid
    grid_size = request.json['grid_size']
    old_grid = gridgame.generateGrid(grid_size, grid_size)
    return jsonify(old_grid)

@app.route('/receive-player-grid', methods=['POST'])
def receiveGridGame():
    new_grid = request.json
    return jsonify(gridgame.compareGrid(old_grid, new_grid))

app.run()