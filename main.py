#!/usr/bin/python
import tensorflow as tf

from config import Config
from model import CaptionGenerator
from dataset import prepare_train_data, prepare_eval_data, prepare_test_data

FLAGS = tf.app.flags.FLAGS

tf.flags.DEFINE_string('phase', 'train',
                       'The phase can be train, eval or test')

tf.flags.DEFINE_boolean('load', False,
                        'Turn on to load a pretrained model from either \
                        the latest checkpoint or a specified file')

tf.flags.DEFINE_string('model_file', None,
                       'If sepcified, load a pretrained model from this file')

tf.flags.DEFINE_boolean('load_cnn', False,
                        'Turn on to load a pretrained CNN model')

tf.flags.DEFINE_string('cnn_model_file', './vgg16_no_fc.npy',
                       'The file containing a pretrained CNN model')

tf.flags.DEFINE_boolean('train_cnn', False,
                        'Turn on to train both CNN and RNN. \
                         Otherwise, only RNN is trained')

tf.flags.DEFINE_integer('beam_size', 3,
                        'The size of beam search for caption generation')


def main(argv):
    config = Config()
    config.phase = FLAGS.phase
    config.train_cnn = FLAGS.train_cnn
    config.beam_size = FLAGS.beam_size
    checkpoint_dir = config.checkpoint_dir
    save_checkpoint_secs = config.save_checkpoint_secs
    save_checkpoint_steps = config.save_checkpoint_steps

    global_step = tf.train.get_or_create_global_step()
    checkpoint_step = tf.assign_add(global_step, 1)
    
    model = CaptionGenerator(config)

    # with tf.Session() as sess:
    with tf.train.MonitoredTrainingSession(checkpoint_dir=checkpoint_dir,
                                           save_checkpoint_steps=save_checkpoint_steps,
                                           ) as sess:
        if FLAGS.phase == 'train':
            # training phase
            data = prepare_train_data(config)
            # WIP modify load part
            # if FLAGS.load:
            #     model.load(sess, FLAGS.model_file)
            # if FLAGS.load_cnn:
            #     model.load_cnn(sess, FLAGS.cnn_model_file)
            model.train(sess, data)

        elif FLAGS.phase == 'eval':
            # evaluation phase
            coco, data, vocabulary = prepare_eval_data(config)
            tf.get_default_graph().finalize()
            model.eval(sess, coco, data, vocabulary)

        else:
            # testing phase
            data, vocabulary = prepare_test_data(config)
            tf.get_default_graph().finalize()
            model.test(sess, data, vocabulary)


if __name__ == '__main__':
    tf.app.run()
