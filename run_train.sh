export PYTHONPATH="./utils/coco/pycocoevalcap:./utils/coco/pycocoevalcap/bleu:$PYTHONPATH:./utils/coco/pycocoevalcap/cider" && \
	python main.py --phase=train \
    	--load_cnn \
    	--cnn_model_file='./vgg16_no_fc.npy'\
    	--train_cnn
