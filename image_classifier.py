#!/usr/bin/python3

import jetson.inference
import jetson.utils
import argparse
import sys


def predict(net, img): 
    # load image from camera
    class_desc = net.GetClassDesc(class_idx)

    print("Prediction: '{:s}' (class #{:d}) with {:f}% confidence".format(class_desc, class_idx, confidence * 100))

    return ImagePrediction(Material(class_idx), confidence) 
