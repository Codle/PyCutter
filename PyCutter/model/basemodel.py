""" 模型基类 """


class Model(object):

    def __init__(self):
        pass

    def cut(self, sentence):
        raise NotImplementedError

    def save(self, path):
        """ 保存模型到指定路径 """
        pass

    def load(self, path):
        pass
