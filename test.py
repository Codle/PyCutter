from WordCutter.vocab import Vocabulary

if __name__ == '__main__':

    vocab = Vocabulary()

    vocab.add("我")
    vocab.add("我的祖国")

    print(vocab.word_num, vocab.node_num)
