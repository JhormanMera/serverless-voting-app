import os
import random
import socket

import funker
from flask import Flask, make_response, render_template, request

option_a = os.getenv('OPTION_A', "Cats")
option_b = os.getenv('OPTION_B', "Dogs")

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def hello():
    vote = None

    if request.method == 'POST':
        vote = request.form['vote']
        funker.call("process-vote", vote=vote)

    resp = make_response(render_template(
        'index.html',
        option_a=option_a,
        option_b=option_b,
        vote=vote,
    ))
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
