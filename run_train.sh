docker --gpus all run -it --rm tensorflow/tensorflow:1.14.0-gpu-py3 \
 -v `pwd`:/workspace
export PYTHONPATH="./utils/coco/pycocoevalcap:./utils/coco/pycocoevalcap/bleu:$PYTHONPATH:./utils/coco/pycocoevalcap/cider" && \
	python main.py --phase=train \
    	--load_cnn \
    	--cnn_model_file='./vgg16_no_fc.npy'\
    	--train_cnn
