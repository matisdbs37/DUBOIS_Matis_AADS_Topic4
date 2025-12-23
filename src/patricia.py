class PatriciaNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class PatriciaTrie:
    def __init__(self):
        self.root = PatriciaNode()

    def insert(self, word):
        node = self.root
        while True:
            for edge, child in node.children.items():
                i = 0
                while i < len(edge) and i < len(word) and edge[i] == word[i]:
                    i += 1
                
                if i > 0:
                    if i == len(edge):
                        word = word[i:]
                        node = child
                        if word == "":
                            node.is_end_of_word = True
                        return
                    
                    new_node = PatriciaNode()
                    new_node.children[edge[i:]] = child
                    new_node.is_end_of_word = False
                    node.children[edge[:i]] = new_node
                    del node.children[edge]

                    if i < len(word):
                        new_node.children[word[i:]] = PatriciaNode()
                        new_node.children[word[i:]].is_end = True
                    else:
                        new_node.is_end = True
                    return

            node.children[word] = PatriciaNode()
            node.children[word].is_end = True
            return

    def search(self, word):
        node = self.root
        while word:
            found = False
            for edge, child in node.children.items():
                if word.startswith(edge):
                    word = word[len(edge):]
                    node = child
                    found = True
                    break
            if not found:
                return False
        return node.is_end_of_word
    
    def range_search(self, prefix):
        results = []

        def dfs(current_node, path):
            if current_node.is_end_of_word:
                results.append(path)
            for edge, child in current_node.children.items():
                dfs(child, path + edge)

        node = self.root
        path = ""
        while prefix:
            matched = False
            for edge, child in node.children.items():
                if prefix.startswith(edge):
                    path += edge
                    prefix = prefix[len(edge):]
                    node = child
                    matched = True
                    break
                elif edge.startswith(prefix):
                    path += edge
                    dfs(child, path)
                    return results
            if not matched:
                return []
            
        dfs(node, path)
        return results
    
    def delete(self, word):
        def recursive_delete(node, word):
            for edge in list(node.children):
                child = node.children[edge]

                if word.startswith(edge):
                    suffix = word[len(edge):]

                    if suffix == "":
                        child.is_end_of_word = False
                    else:
                        recursive_delete(child, suffix)

                    if not child.children and not child.is_end_of_word:
                        del node.children[edge]
                        return

                    if not child.is_end_of_word and len(child.children) == 1:
                        next_edge, next_child = next(iter(child.children.items()))
                        node.children[edge + next_edge] = next_child
                        del node.children[edge]

                    return

        recursive_delete(self.root, word)