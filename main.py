import pickle
from word_cutter import dag
from word_cutter.finalseg import cut
import pprint
from word_cutter import trie
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-sentence', type=str, help='a sentence')
args = parser.parse_args()


if __name__ == '__main__':
    route = {}
    trie_tree = pickle.load(open('trie.pkl', 'rb'))

    trie_tree.init_dict()
    DAG = dag.DAG(trie_tree.dict)

    sentence = args.sentence
    dag = DAG.get_dag(sentence)
    print('DAG:', dag)
    route = DAG.calc_prob(sentence, dag, route)
    print('Route:')
    pprint.pprint(route)
    result = ''
    i = 0
    while i < len(sentence):

        result += sentence[i:route[i][1]+1] + '/'
        i = route[i][1]+1
    print(result)

    hmm_res = ''
    for w in cut(sentence):
        hmm_res += w + '/'

    print('HMM:', hmm_res)
