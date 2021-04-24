# Split Ratio: (training, validation) or (training, validation, test) 

import os 
import splitfolders  # or import split_folders

ratio = (.8, .2)
seed = 1337 

jetson_path="~/jetson-inference/python/training/classification"
input_folder = "kaggle/GarbageClassificaton/GarbageClassification/"
output_folder = jetson_path + "/data/GarbageClassification"

splitfolders.ratio(input_folder, output=output_folder, seed=seed, ratio=ratio, group_prefix=None) 
