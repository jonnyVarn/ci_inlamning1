#import os
#import subprocess
from flask import Flask, render_template
#from flask import Response, request
#from flask_api import status

#create Flask instance
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("Hello")
def ip():
    return reqests.host()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
