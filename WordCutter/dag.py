from math import log
from xlwings import xrange


class DAG(object):
    def __init__(self, freq):
        self.total = 0
        for key in freq.keys():
            self.total += freq[key]
        self.FREQ = freq

    def get_dag(self, sentence):
        dag = {}
        n = len(sentence)
        keys = self.FREQ.keys()

        for k in range(n):
            temp = []
            i = k
            frag = sentence[k]

            while i < n and frag in keys:
                if self.FREQ[frag]:
                    temp.append(i)
                i += 1
                frag = sentence[k:i + 1]
            if not len(temp):
                temp.append(k)

            dag[k] = temp
        return dag

    def calc_prob(self, sentence, dag, route):
        n = len(sentence)
        route[n] = (0, 0)
        log_total = log(self.total)
        # 从后往前遍历句子 反向计算最大概率
        for idx in xrange(n - 1, -1, -1):
            # 列表推倒求最大概率对数路径
            # route[idx] = max([ (概率对数，词语末字位置) for x in DAG[idx] ])
            # 以idx:(概率对数最大值，词语末字位置)键值对形式保存在route中
            # route[x+1][0] 表示 词路径[x+1,N-1]的最大概率对数,
            # [x+1][0]即表示取句子x+1位置对应元组(概率对数，词语末字位置)的概率对数

            # 原则上用这个即可，后面的是为了方便理解
            # route[idx] = max((log(self.FREQ.get(sentence[idx:x + 1]) or 1) -
            #                   log_total + route[x + 1][0], x) for x in dag[idx])

            max_idx = 0
            max_pro = -99999
            for x in dag[idx]:
                if sentence[idx:x + 1] in self.FREQ.keys():
                    pro = log(self.FREQ.get(sentence[idx:x + 1]))
                else:
                    pro = 0
                pro -= log_total
                pro += route[x + 1][0]
                if pro > max_pro:
                    max_pro = pro
                    max_idx = x
            route[idx] = (max_pro, max_idx)
        return route

