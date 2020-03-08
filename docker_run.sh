docker run --gpus all -it --rm \
 -v `pwd`:/workspace \
 -v /home/jie/nltk_data:/usr/lib/nltk_data \
 -v /data/dataset/coco/train2014:/workspace/train/images \
 -v /data/dataset/coco/val2014:/workspace/val/images \
 tensorflow/tensorflow:1.14.0-gpu-py3 bash
