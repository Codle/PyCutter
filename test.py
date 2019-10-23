from PyCutter.vocab import Vocabulary
from PyCutter.model.ngram import NGram

if __name__ == '__main__':

    vocab = Vocabulary()

    vocab.add("南")
    vocab.add("南京")
    vocab.add("南京市")
    vocab.add("京")
    vocab.add("市")
    vocab.add("市长")
    vocab.add("长")
    vocab.add("长江")
    vocab.add("江")
    vocab.add("大")
    vocab.add("大桥")
    vocab.add("桥")
    model = NGram()
    for i in model.cut("南京市长江大桥", vocab):
        print(i)
