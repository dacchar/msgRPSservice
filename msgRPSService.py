import logging
import json
from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



@app.route('/print')
@cross_origin()
def print_msg():
    app.logger.debug('Just the test.')
    return "Check your console"


@app.route('/sendStatus', methods=['GET', 'POST', 'PUT'])
@cross_origin()
def send_status():
    app.logger.debug('Event: ')

    req_data = request.get_json()
    game_id = req_data['gameId']
    leader_id = req_data['leaderId']
    leader_name = req_data['leaderName']
    hit = req_data['hit']
    mode = req_data['mode']

    status = req_data['status']
    app.logger.debug('Game id: ' + str(game_id))
    app.logger.debug('Leader id: ' + str(leader_id))
    app.logger.debug('Leader name: ' + leader_name)
    app.logger.debug('Status: ' + status)
    app.logger.debug('Hit: ' + str(hit))
    app.logger.debug('Mode: ' + mode)
    
    # a = {'Status': 'OK'}
    a = {'status': 'OK', 'hit': 1}
    python2json = json.dumps(a)

    return python2json


@app.route('/getAIHit', methods=['GET'])
@cross_origin()
def get_ai_hit():
    app.logger.debug('get AI hit')
    
    hit = {'hit': 1}
    python2json = json.dumps(hit)

    return python2json


@app.route("/")
@cross_origin()
def hello():
    return "Hello from msgRPSService!"


if __name__ == '__main__':
    app.run(debug=True)
