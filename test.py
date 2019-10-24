from PyCutter.vocab import Vocabulary
from PyCutter.model import UniGramModel
from PyCutter.utils.data import load_words_from_dir


if __name__ == '__main__':

    vocab = Vocabulary()
    train_path = 'data/icwb2-data/training'

    words = load_words_from_dir(train_path, '.utf8')
    for word in words:
        vocab.add(word)

    model = UniGramModel()
    model.cut("南京市长江大桥", vocab)
