""" 模型基类 """
import pickle


class Model(object):

    def __init__(self):
        pass

    def save(self, path):
        """ 保存模型到指定路径 """
        with open(path, 'wb') as f:
            pickle.dump(self, f)
