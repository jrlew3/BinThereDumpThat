#!/usr/bin/python3

import jetson.inference
import jetson.utils
import argparse
import sys
from lib import prediction


def predict(net, img, output): 
    # Get prediction
    class_idx, confidence = net.Classify(img)
    class_desc = net.GetClassDesc(class_idx)

    print("Image Prediction: '{:s}' (class #{:d}) with {:f}% confidence".format(class_desc, class_idx, confidence * 100))

    return prediction.ImagePrediction(prediction.Material(class_idx), confidence) 
