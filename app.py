# import os
# import subprocess
# from flask import render_template
import socket
from flask import Response, Request, Flask

# from flask_api import status


app = Flask(__name__)
hostname = socket.gethostname()



@app.route('/test')
    def test():
    return 'ok'

@app.route('/', methods=['POST', 'GET'])
def container():
    return f'its working {hostname}'


@app.route('/headers')
def headers():
    result = ""
    for header in request.headers:
        result = result + f'{header[0]}:\t{header[1]}\n'
    return Response(result, mimetype='text/plain')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

    # i hate pep8..
