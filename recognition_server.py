from flask import Flask, url_for, request
from werkzeug.utils import secure_filename
import os
import sys
import cv2
import numpy as np
import threading

app = Flask(__name__)

## set FLASK_APP=recognition_server.py
## python -m flask run --host=127.0.0.1:5000
## ngrok 5000

global RECORD

def record_video(vid_dir, fname, webcam_num=0):
    cap = cv2.VideoCapture(webcam_num, cv2.CAP_DSHOW)
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('{}.avi'.format(vid_dir + fname), fourcc, 20.0, (640,480))
    
    global RECORD
    RECORD = True
    while(RECORD):
        ret, frame = cap.read()
        out.write(frame)
        cv2.imshow('gait_capture_playback', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return True

@app.route('/')
def hello():
    return "Immobile Computing's Final Project"

@app.route('/testget', methods=['GET'])
def test_get():
    if(request.method == 'GET'):
        return "successfully pinged the server"
    else:
        print("invalid request made by client")
    return "invalid request made - please try again"

@app.route('/senddata', methods=['POST'])
def send_data():
    DATA_DIR = "mobile_data/"

    if(request.method == 'POST'):
        # print("testing\n", request.get_data(as_text = True))
        files = request.files
        # print(files)
        for tempf in files.keys():
            f = request.files[tempf]
            try:
                f.save(DATA_DIR + secure_filename(f.filename))
            except: 
                print("failed to save the file")
                return "Failed to recieve the file"
        return "Successfully downloaded file"
    else:
        print("Invalid request made")
        return "THIS IS NOT WORKING!!!!"


@app.route('/record/<fname>', methods=['GET'])
def record(fname):
    # tmpt = threading.Thread(target=record_video, args=('video_data/', fname, 0))
    tmpt = threading.Thread(target=record_video, args=('video_data/', fname, 1))
    tmpt.start()
    print("started recording and saving to {}".format(fname))
    return "Started Recording"

@app.route('/stop_record', methods=['GET'])
def stop_record():
    global RECORD
    RECORD = False
    return ("stopped recording")

@app.route('/listfiles', methods=['GET'])
def list_files():
    DATA_DIR = "mobile_data/"

    if(request.method == 'GET'):
        print("request to see the files in our classification server")
        temp = os.listdir(DATA_DIR)
        total = ""
        for f in temp:
            total = total + " ; " + f 
        return total
    else:
        print("invalid request made")
        return "ERROR"

@app.route('/listvids', methods=['GET'])
def list_vids():
    DATA_DIR = "video_data"

    if(request.method == 'GET'):
        print("request to see the files in our classification server")
        temp = os.listdir(DATA_DIR)
        total = ""
        for f in temp:
            total = total + " ; " + f 
        return total
    else:
        print("invalid request made")
        return "ERROR"


@app.route('/classify', methods=['POST'])
def classify():
    raise NotImplementedError

 