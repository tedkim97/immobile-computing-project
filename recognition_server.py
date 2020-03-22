from flask import Flask, url_for, request
from werkzeug.utils import secure_filename
import os
import sys
import cv2
import numpy as np
import threading

# Reminder for running the flask script
# "set FLASK_APP=recognition_server.py"
# "python -m flask run --host=127.0.0.1:5000"
# "ngrok 5000"


app = Flask(__name__)


global RECORD # Global variable that defines the recording state of our setup
# This will not really work well if there are multiple requests being made 
# (because of the mulithreading applications); however, for our purpose it should
# be OK 

def record_video(vid_dir, fname, webcam_num=0):
    """
    Helper function to signal the server to start recording video with opencv
    """
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
    """
    testing functionality
    """
    if(request.method == 'GET'):
        return "successfully pinged the server"
    else:
        print("invalid request made by client")
    return "invalid request made - please try again"

@app.route('/senddata', methods=['POST'])
def send_data():
    """
    function to receive the csv files recorded on a phone
    """
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
    """
    signal to automatically label and record a video file with a GET request
    """
    tmpt = threading.Thread(target=record_video, args=('video_data/', fname, 1))
    tmpt.start()
    print("started recording and saving to {}".format(fname))
    return "Started Recording"

@app.route('/stop_record', methods=['GET'])
def stop_record():
    """
    function to stop recording by flipping RECORD to false
    """
    global RECORD
    RECORD = False
    return ("stopped recording")

@app.route('/listfiles', methods=['GET'])
def list_files():
    """
    testing function that lets the requestee see what files are on the server
    """
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
    """
    testing function that lets the reqestee see what videos are on the server
    """
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

 