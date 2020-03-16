import numpy as np
import torch
import os
import sys

def pre_process_csv(fname):
    data = None
    with open(fname, 'r') as f:
        data = np.genfromtxt(fname)
    return data


def main():
    return True

if __name__ == "__main__":
    SENSOR_DIR = "data/mobile_data/"
    VID_DIR = "data/video_data/" 
    print(os.listdir(SENSOR_DIR))
    print(os.listdir(VID_DIR))
    print("test")