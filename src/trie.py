class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True

    def search(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end_of_word
    
    def range_search(self, prefix):
        node = self.root
        results = []

        for char in prefix:
            if char not in node.children:
                return results
            node = node.children[char]

        def dfs(current_node, path):
            if current_node.is_end_of_word:
                results.append(path)
            for char, child_node in current_node.children.items():
                dfs(child_node, path + char)
        
        dfs(node, prefix)

        return results
    
    def delete(self, word):
        def recursive_delete(node, i):
            if i == len(word):
                node.is_end_of_word = False
                return len(node.children) == 0
            char = word[i]
            if char in node.children and recursive_delete(node.children[char], i + 1):
                del node.children[char]
                return not node.is_end_of_word and len(node.children) == 0
            return False
        
        recursive_delete(self.root, 0)