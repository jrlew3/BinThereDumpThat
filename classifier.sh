JETSON=~/jetson-inference/python/training/classification
NET=$JETSON/models/GarbageClassification
DATASET=$JETSON/data/GarbageClassification
IMAGENET=~/jetson-inference/build/aarch64/bin 

cd $IMAGENET
./imagenet --model=$NET/resnet50.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt csi://0
cd ~/BinThereDumpThat
