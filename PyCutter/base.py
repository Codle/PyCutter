# 基本功能函数
import pickle
from PyCutter import model
import os
import sys


class Cutter(object):

    def __init__(self, method='unigram'):
        self.method = method
        vocab_file = os.path.join(
            os.path.dirname(sys.modules[__package__].__file__),
            'resource/icwb2_vocab.pickle')
        with open(os.path.join(vocab_file), 'rb') as f:
            self.vocab = pickle.load(f)
        self.model = model.UniGramModel()

    def cut(self, sentence):
        return self.model.cut(sentence, self.vocab)
