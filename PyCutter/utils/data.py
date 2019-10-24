import os


def load_words_from_file(file_path, encoding='utf8'):
    with open(file_path, encoding=encoding) as f:
        words = f.read().split()
    return words


def load_words_from_dir(dir_path, file_end_with='', encoding='utf8'):
    file_paths = os.listdir(dir_path)
    words = []
    for file_path in file_paths:
        if file_path[-len(file_end_with):] == file_end_with:
            words += load_words_from_file(dir_path+'/'+file_path, encoding)

    return words
