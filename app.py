import os
#import subprocess
import socket
from flask import Flask, render_template
from flask import Response, request
from flask_api import status


#create Flask instance
app = Flask(__name__)



@app.route('/')



@app.route('/', methods=['POST'])
def containerRunning():
    hostname = socket.gethostname()
    return f'its working {hostname} \n'
    
@app.route('/headers')
    def headers():
        for header in request.headers:
            result = result + f'{header[0]}:\t{header[1]}\n'
            return Response(result, mimetype='text/plain')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
