# pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
# apt update && apt install -y libsm6 libxext6
# apt-get install libxrender1
export PYTHONPATH="./utils/coco/pycocoevalcap:./utils/coco/pycocoevalcap/bleu:$PYTHONPATH:./utils/coco/pycocoevalcap/cider" && \
	python main.py --phase=train \
    	--train_cnn
