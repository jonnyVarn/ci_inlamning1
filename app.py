import socket
from flask import Response, Request, Flask


app = Flask(__name__)
hostname = socket.gethostname()


@app.route('/test')
def testar():
    return 'ok'


@app.route('/', methods=['POST', 'GET'])
def container():
    return f'its working {hostname}'


@app.route('/headers')
def headers():
    result = ""
    for header in Request.headers:
        result = result + f'{header[0]}:\t{header[1]}\n'
    return Response(result, mimetype='text/plain')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
