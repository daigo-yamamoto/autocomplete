class TrieNode:
    def __init__(self):
        self.children = {}  # Dicionário para armazenar filhos
        self.is_end_of_word = False  # Indica se é o fim de uma palavra

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def autocomplete(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []  # Prefixo não encontrado
            current = current.children[char]
        return self._find_words(prefix, current)

    def _find_words(self, prefix, node):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            words.extend(self._find_words(prefix + char, child_node))
        return words
