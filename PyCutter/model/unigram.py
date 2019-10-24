""" N-Gram 模型实现

Author: Yin
Date: 2019/10/20
"""

from math import log

import networkx as nx

from .basemodel import Model
from ..vocab import Vocabulary


class UniGramModel(Model):

    def __init__(self, n_gram=1):
        self.n_gram = n_gram

    def cut(self, sentence: str, vocab: Vocabulary):
        """ 求取句子中所有的词组合 """
        sentence_freq = []
        for i in range(len(sentence)):
            # 不使用+=操作，这样可以额外获得启示点位置索引
            sentence_freq.append(vocab.find_prefix(sentence[i:]))

        edges = []
        # 转换生成边
        for idx, word_freqs in enumerate(sentence_freq):
            for (word, freq) in word_freqs:
                edge = ((idx, idx+len(word), log(freq/vocab.freq)))
                edges.append(edge)

        # 创建 DAG
        G = nx.DiGraph()
        G.add_nodes_from(range(len(sentence)+1))
        G.add_weighted_edges_from(edges)

        # dp
        end_idx = len(sentence)-1
        route = [None for i in range(len(sentence))]
        prob = [None for i in range(len(sentence))]

        for i in range(end_idx, -1, -1):
            # TODO: 需要修改
            max_prob = -999999
            for next_idx in G[i]:
                if next_idx == len(sentence):
                    cur_prob = G[i][next_idx]['weight']
                else:
                    cur_prob = G[i][next_idx]['weight'] + prob[next_idx]

                if cur_prob > max_prob:
                    max_prob = cur_prob
                    prob[i] = max_prob
                    route[i] = next_idx

        start_idx = 0
        while start_idx != len(sentence):
            yield sentence[start_idx: route[start_idx]]
            start_idx = route[start_idx]
