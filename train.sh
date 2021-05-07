JETSON=~/jetson-inference/python/training/classification
NET=$JETSON/models/GarbageClassification
DATASET=$JETSON/data/GarbageClassification
IMAGENET=~/jetson-inference/build/aarch64/bin 

cd $JETSON 
python3 train.py -a=resnet50 --epochs=60 --model-dir=models/GarbageClassification data/GarbageClassification

cd ~/BinThereDumpThat
