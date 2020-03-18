import numpy as np
import torch
import os
import sys

def preprocess_csv(fname, names, nmap,delim=',', skip_line=1):
    """
    Function that takes a csv and and turns it into a numpy array
    by content and label by filename
    
    fname : (str) the csv name
    names : (set) names that will indicate the label
    nmap : (dict) mapping of name to index -
    delim : (str) delimiter used in the csv
    skip_line : (int) number of lines to skip (for headers)
    """
    label = None
    features = None
    
    for x in names:
        if (x in fname.lower()):
            label = np.array(nmap[x])
            
    with open(fname, 'r') as f:
        features = np.genfromtxt(fname,delimiter=delim,skip_header=skip_line)
    return features, label

def generate_features(mob_dir,names,nmap,delim=',', skip_line=1):
    """
    Function that takes all the files in a directory and turns 
    them into a list of numpy features and labels
    
    mob_dir : (str) directory of csv's
    --- rest are the same parameters as preprocess_csv
    names : (list) names that will indicate the label
    """
    files = os.listdir(mob_dir)
    features, labels = [],[]

    for fname in files:
        tempf, templ = preprocess_csv(mob_dir + fname, names, \
                                      nmap,delim=delim, skip_line=skip_line)
        features.append(tempf)
        labels.append(templ)
    
    return np.array(features), np.array(labels)

def reduce_feature_shape(feats, labels, min_len):
    """
    Function that a given feature tensor and label vector
    and cuts out all features/labels that don't meet the 
    required minimum_length, and changes all tensors 
    to meet that minimum 
    
    feats : (numpy 3d tensor)
    labels : (numpy vector)
    min_len: (int) minimum length of feature-matrix
    """
    fprime, lprime = [], []
    for pre_feat, labl in zip(feats, labels):
        if(pre_feat.shape[0] >= min_len):
            cutoff = pre_feat.shape[0] - min_len
            post_feat = pre_feat[cutoff:,]
            fprime.append(post_feat)
            lprime.append(labl)
            
    return np.array(fprime), np.array(lprime)


def main():
    return True

if __name__ == "__main__":
    SENSOR_DIR = "data/mobile_data/"
    VID_DIR = "data/video_data/" 
    print(os.listdir(SENSOR_DIR))
    print(os.listdir(VID_DIR))
    print("test")