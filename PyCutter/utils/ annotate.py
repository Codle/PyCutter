""" 序列标注工具
"""


def label_seuqnece(file):
    fin = open(file, 'r')
    vocab = set()
    pair_sequence = []
    for line in fin.readlines():
        words = line.split(' ')
        labels = []
        for word in words:
            if len(word) == 1:
                labels.append('S')
            else:
                label = 'M'*len(word)
                label[0] = 'B'
                label[-1] = 'E'
                labels.append(label)
        pair_sequence.append((''.join(words)))
    return pair_sequence
