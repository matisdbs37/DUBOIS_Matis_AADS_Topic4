from graphviz import Digraph

# Visualize a Trie or Patricia Trie using Graphviz and save as PDF
def visualize_trie(trie, filename):
    dot = Digraph() # Create a new Graphviz Digraph object
    dot.attr('node', shape='circle', label='') # Set all nodes to be circles with no labels

    # Recursive function to traverse the trie and add nodes/edges to the graph
    def dfs(node):
        node_id = str(id(node)) # Unique ID for each node
        dot.node(node_id) # Add the current node to the graph

        # Iterate over all children of the current node
        for edge, child in node.children.items():
            # Add child node with unique ID to the graph and draw edge from parent to child, with edge label
            child_id = str(id(child))
            dot.node(child_id)
            dot.edge(node_id, child_id, label=edge)
            dfs(child)

    dfs(trie.root) # Start DFS traversal from the root
    dot.render(filename, cleanup=True) # Render graph to PDF file
