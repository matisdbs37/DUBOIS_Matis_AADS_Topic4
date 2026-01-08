# Node of a Patricia Trie
class PatriciaNode:
    def __init__(self):
        self.children = {} # Dictionary mapping edges (strings) to Patricia nodes
        self.is_end_of_word = False # True if node represents end of a word, else False

# Patricia Trie data structure
class PatriciaTrie:
    def __init__(self):
        self.root = PatriciaNode() # Root node of the Patricia Trie

    # Insert a word into the Patricia Trie
    def insert(self, word):
        node = self.root # Start at root

        while True:
            # Try to find an edge that matches the start of the word
            for edge, child in node.children.items():
                i = 0
                # Find the length of the common prefix between edge and word
                while i < len(edge) and i < len(word) and edge[i] == word[i]:
                    i += 1
                
                # If there is a common prefix
                if i > 0:
                    # If the edge fully matches the word, move down that edge
                    if i == len(edge):
                        word = word[i:] # Remove matched part from word
                        node = child # Move to the child node
                        # if word is now empty, mark this node as end of word because the word is fully inserted
                        if word == "":
                            node.is_end_of_word = True
                        return
                    
                    # If we reached here, we only have a partial match, need to split the edge
                    new_node = PatriciaNode()
                    new_node.children[edge[i:]] = child # Existing child becomes child of new node
                    new_node.is_end_of_word = False
                    node.children[edge[:i]] = new_node # Common prefix becomes new edge
                    del node.children[edge] # Remove old edge

                    # If word has remaining letters
                    if i < len(word):
                        # Add the remaining part of the word as a new child
                        new_node.children[word[i:]] = PatriciaNode()
                        new_node.children[word[i:]].is_end_of_word = True
                    # If no remaining letters, mark new node as end of word
                    else:
                        new_node.is_end_of_word = True
                    return

            # If we reached here, no matching edge found, so add the whole word as a new edge
            node.children[word] = PatriciaNode()
            node.children[word].is_end_of_word = True
            return

    # Search for a word in the Patricia Trie
    def search(self, word, print_result=True):
        node = self.root # Start at root
        word_copy = word # Copy of the word for printing

        # While there are still letters left in the word
        while word:
            found = False # Flag to indicate if a matching edge was found

            # Try to find an edge that matches the start of the word
            for edge, child in node.children.items():
                # If the word starts with an edge, follow that edge and continue with the remaining part of the word
                if word.startswith(edge):
                    word = word[len(edge):]
                    node = child
                    found = True
                    break

            # If no matching edge found, word is not in the trie
            if not found:
                if print_result:
                    print(word_copy, "not found in Patricia trie.")
                return False
        
        # If we reached here, word exists in the Patricia trie if current node marks end of word
        if print_result:
            if node.is_end_of_word:
                print(word_copy, "found in Patricia trie.")
            else:
                print(word_copy, "not found in Patricia trie.")
        return node.is_end_of_word
    
    # Find all words in the Patricia Trie that start with a given prefix
    def range_search(self, prefix, print_result=True):
        results = []  # List to store found words
        node = self.root # Start at root
        path = "" # To build the current path
        prefix_copy = prefix  # Copy of the prefix for printing

        # Traverse the Patricia trie to reach the end of the prefix
        while prefix:
            # Try to find an edge that matches the start of the prefix
            for edge, child in node.children.items():
                # If the prefix starts with the edge, follow that edge
                if prefix.startswith(edge):
                    path += edge
                    prefix = prefix[len(edge):]
                    node = child
                    break

                # If the edge starts with the prefix, it means we have found the prefix
                elif edge.startswith(prefix):
                    path += edge
                    node = child
                    prefix = "" # Prefix is fully matched
                    break

            # If no matching edge found, the prefix doesn't exist
            else:
                if print_result:
                    print("No words found with prefix", prefix_copy)
                return False

        # From the end of the prefix, do a DFS to find all words
        def dfs(current_node, current_path):
            # If the current node marks end of a word, word can be added to results
            if current_node.is_end_of_word:
                results.append(current_path)

            # Recursively visit all children with updated path
            for edge, child in current_node.children.items():
                dfs(child, current_path + edge)

        dfs(node, path)  # Start DFS from the end of the prefix
        
        # Print results or indicate no words found
        if print_result:
            if results:
                print("Words with prefix", prefix_copy, ":", results)
            else:
                print("No words found with prefix", prefix_copy)
        return node.is_end_of_word

    # Delete a word from the Patricia Trie
    def delete(self, word):
        # Function for recursive deletion
        def recursive_delete(node, word):
            # Iterate over all children of the current node
            for edge in list(node.children):
                child = node.children[edge]

                # If the word starts with the edge
                if word.startswith(edge):
                    # Remaining part of the word
                    suffix = word[len(edge):]

                    # If the entire edge matches the word, we need to delete from this child
                    if suffix == "":
                        child.is_end_of_word = False
                    # Else, recurse on the child with the remaining word
                    else:
                        recursive_delete(child, suffix)

                    # Remove child if it has no children and is not end of another word
                    if not child.children and not child.is_end_of_word:
                        del node.children[edge]
                        return
                    
                    # If after deletion the child has only one child and is not end of a word, merge edges
                    if not child.is_end_of_word and len(child.children) == 1:
                        next_edge, next_child = next(iter(child.children.items()))
                        node.children[edge + next_edge] = next_child
                        del node.children[edge]

                    return

        # Start recursive deletion from root and the word to delete
        recursive_delete(self.root, word)