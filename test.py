import PyCutter
import tqdm
import pickle


if __name__ == '__main__':

    cutter = PyCutter.Cutter()
    ans_file = open('output/ans.utf8', 'w')
    with open('data/testing/pku_test.utf8', 'r') as  test_file:
        for line in tqdm.tqdm(test_file.readlines()):
            words = cutter.cut(line)
            ans_file.write(' '.join(words))
    ans_file.close()
