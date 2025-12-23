from graphviz import Digraph

def visualize_trie(trie, filename):
    dot = Digraph()
    dot.attr('node', shape='circle', label='')

    counter = 0
    node_ids = {}

    def get_node_id(node):
        nonlocal counter
        if node not in node_ids:
            node_ids[node] = f"n{counter}"
            dot.node(node_ids[node], label="")
            counter += 1
        return node_ids[node]

    def dfs(node):
        parent_id = get_node_id(node)
        for c, child in node.children.items():
            child_id = get_node_id(child)
            dot.edge(parent_id, child_id, label=c)
            dfs(child)

    dfs(trie.root)
    dot.render(filename)
