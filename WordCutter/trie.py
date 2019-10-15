import pickle


class TrieNode(object):
    """ 树节点 """
    def __init__(self, char: str):
        self.value = char
        self.children = []
        self.finished = False
        self.counter = 1


class TrieTree(object):

    def __init__(self, root_val = ''):
        self.root = TrieNode(root_val)
        self.dict = {}

    def add(self, word: str):
        """ 添加词语 """
        node = self.root
        for char in word:
            found_in_child = False
            for child in node.children:
                if child.char == char:
                    child.counter += 1
                    node = child
                    found_in_child = True
                    break
            if not found_in_child:
                new_node = TrieNode(char)
                node.children.append(new_node)
                node = new_node
        node.finished = True

    def find_prefix(self, prefix: str):
        
        node = self.root

        if not self.root.children:
            return False, None
        for char in prefix:
            char_not_found = True
            for child in node.children:
                if child.char == char:
                    char_not_found = False
                    node = child
                    break
            if char_not_found:
                return False, None

        return True, node

    def init_dict(self, node=None, word=''):
        """构造词典
        参数:
            node: 当前节点
            word: 当前的单词
        返回值:
            无
        """
        if not node:
            node = self.root

        if node.finished:
            self.dict[word] = node.counter

        if len(node.children):

            for child in node.children:
                self.init_dict(child, word + child.char)

    def save_dict(self, path='data/dict.pkl'):
        pickle.dump(self.dict, open(path, 'wb'))

    def load_dict(self, path='data/dict.pkl'):
        self.dict = pickle.load(open(path, 'rb'))
