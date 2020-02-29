from flask import Flask, url_for, request
from werkzeug.utils import secure_filename
import os
import sys

app = Flask(__name__)

## expot FLASK_APP = recognition_server.py
## python -m flask run --host=127.0.0.1:5000
## ngrok 5000


@app.route('/')
def hello():
    return "Immobile Computing's Final Project"

@app.route('/sendData', methods=['POST'])
def sendData():
    DATA_DIR = "classification_data/"

    if(request.method == 'POST'):
        print("Post request made to send data")
        files = request.files
        for tempf in files.keys():
            f = request.files[tempf]
            try:
                f.save(DATA_DIR + secure_filename(f.filename))
            except: 
                print("failed to save the file")
                return "Failed to recieve the file"
        print(os.listdir(DATA_DIR))
        return "Successfully downloaded file"
    else:
        print("Invalid request made")
        return "THIS IS NOT WORKING!!!!"
