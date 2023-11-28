from graphviz import Digraph
import fst
import trie

def visualize_trie(trie):
    def add_nodes_edges(node, node_label):
        if node.is_end_of_word:
            graph.node(node_label, shape='doublecircle')
        for char, child_node in node.children.items():
            child_label = f"{node_label}{char}"
            graph.edge(node_label, child_label, label=char)
            add_nodes_edges(child_node, child_label)

    graph = Digraph()
    graph.node("", shape='point')
    add_nodes_edges(trie.root, "")
    return graph

def visualize_fst(fst):
    def add_nodes_edges(node, node_label):
        if node.is_final:
            graph.node(node_label, shape='doublecircle')
        for char, child_node in node.transitions.items():
            child_label = f"{node_label}{char}"
            graph.edge(node_label, child_label, label=char)
            add_nodes_edges(child_node, child_label)

    graph = Digraph()
    graph.node("", shape='point')
    add_nodes_edges(fst.root, "")
    return graph

def load_words_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

# Carrega as palavras do arquivo
file_path = './dicionario/teste.txt'  # Substitua pelo caminho correto do seu arquivo
words = load_words_from_file(file_path)

# Instanciando e preenchendo a Trie e o FST
trie = trie.Trie()
fst = fst.FST()
for word in words:
    trie.insert_word(word)
    fst.insert_word(word, "")

trie_graph = visualize_trie(trie)
fst_graph = visualize_fst(fst)

trie_graph.render('trie_visualization', view=True)
fst_graph.render('fst_visualization', view=True)
