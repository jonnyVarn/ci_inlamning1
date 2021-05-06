from flask import Flask
from flask import Response, request
from flask_api import status

#create Flask instance
app = Flask(__name__)

@app.route('/')
def hello_World():
    hostname = socket.gethostname()
    return f'Hello World container{hostname}'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)