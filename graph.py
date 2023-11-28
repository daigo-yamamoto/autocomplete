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
    def add_nodes_edges(node_id, node_label, graph):
        node = fst.states[node_id]  # Busca o objeto de estado real usando o ID
        if node.is_final:
            graph.node(node_label, shape='doublecircle')
        for char, child_node_id in node.transitions.items():
            child_label = f"{node_label}{char}"
            graph.edge(node_label, child_label, label=char)
            add_nodes_edges(child_node_id, child_label, graph)  # Passa o ID do filho

    graph = Digraph()
    graph.node("", shape='point')
    add_nodes_edges(fst.root.id, "", graph)  # Passa o ID do nó raiz
    return graph


def load_words_and_outputs(file_path):
    with open(file_path, 'r') as file:
        words_outputs = [line.strip().split() for line in file]
    return words_outputs

# Caminho para o seu arquivo de texto
file_path = './dicionario/teste.txt'
words = load_words_and_outputs(file_path)

# Instanciando e preenchendo a Trie e o FST
trie = trie.Trie()
fst = fst.FST()
for word, output in words:
    trie.insert_word(word)
    fst.insert_word(word, output)

trie_graph = visualize_trie(trie)
fst_graph = visualize_fst(fst)

trie_graph.render('trie_visualization', view=True)
fst_graph.render('fst_visualization', view=True)
