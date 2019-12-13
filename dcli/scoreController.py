import os
import logging
from flask import Flask, request, jsonify
from .const import API_PORT, MISSION_USER_SCORE_ENDPOINT
from .logger import info, error

app = Flask(__name__)

@app.route(MISSION_USER_SCORE_ENDPOINT, methods=['POST'])
def postScore():
    json = request.get_json(force=True) 
    # force=True, above, is necessary if another developer 
    # forgot to set the MIME type to 'application/json'
    if 'score' in json:
        info(f"Score posted by your mission: {json['score']}")
    return ('', 200)

def startScoreResource():
    # disable all logs
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    os.environ['WERKZEUG_RUN_MAIN'] = 'true'
    app.run(debug=False, port=API_PORT)
