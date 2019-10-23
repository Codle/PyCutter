""" 基于 Trie 树的词典实现
Author： Yin
Date： 2019/10/19
"""
from .utils.list import KeyCompareList as KCL


class CharNode(object):
    """ 字符节点 """

    def __init__(self, char):
        self.char = char
        self.finished = False
        self.child = KCL(CharNode, 'char')
        self.count = 1

    def __eq__(self, other):
        return self.char == other


class Vocabulary(object):

    def __init__(self):
        self.root_node = CharNode('#')
        self.node_num = 0
        self.word_num = 0
        self.freq = 0

    def add(self, word: str):
        """ 添加词语：新词则新建节点，旧词就只+1 """

        node = self.root_node

        for char in word:
            self.freq += 1
            if char in node.child:
                node = node.child[char]
                node.count += 1
            else:
                new_node = CharNode(char)
                node.child.append(new_node)
                node = new_node
                self.node_num += 1

        if not node.finished:
            node.finished = True
            self.word_num += 1

    def find_prefix(self, sentence: str):
        """ 前缀查找，查询开头的全部词语 """
        word_freq = []

        node = self.root_node

        for idx, char in enumerate(sentence):
            if char in node.child:
                node = node.child[char]
                if node.finished:
                    word_freq.append((sentence[:idx+1], node.count))
            else:
                break
        return word_freq

    def __len__(self):
        return self.word_num

    def __getitem__(self, word):
        node = self.root_node

        for char in word:
            if char in node.child:
                node = node.child[char]
            else:
                raise KeyError

        if not node.finished:
            raise KeyError

        return node.count
