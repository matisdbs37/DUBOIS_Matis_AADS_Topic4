# Node of a Trie
class TrieNode:
    def __init__(self):
        self.children = {} # Dictionary mapping character to Trie node
        self.is_end_of_word = False # True if node represents end of a word, else False

# Trie data structure
class Trie:
    def __init__(self):
        self.root = TrieNode() # Root node of the Trie

    # Insert a word into a Trie
    def insert(self, word):
        node = self.root # Start at root

        # For each character in the word
        for char in word:
            # If character not present, create a new node
            if char not in node.children:
                node.children[char] = TrieNode()
            
            # Move to the child node
            node = node.children[char]
        
        # Mark the end of the word
        node.is_end_of_word = True

    # Search for a word in the Trie
    def search(self, word, print_result=True):
        node = self.root # Start at root

        # For each character in the word
        for char in word:
            # If character not found, word doesn't exist so return False to stop the search
            if char not in node.children:
                if print_result:
                    print(word, "not found in trie.")
                return False
            
            # Move to the child node
            node = node.children[char]

        # If we reached here, all characters were found so let's check if it's an end of a word
        if print_result:
            if node.is_end_of_word:
                print(word, "found in trie.")
            else:
                print(word, "not found in trie.")
    
    # Find all words in the Trie that start with a given prefix
    def range_search(self, prefix, print_result=True):
        node = self.root # Start at root
        results = [] # List to store found words

        # Traverse the Trie to the end of the prefix
        for char in prefix:
            # If character not found, the prefix doesn't exist so no word can match
            if char not in node.children:
                if print_result:
                    print("No words found with prefix", prefix)
                return results # Return empty list
            
            # Move to the child node
            node = node.children[char]

        # From the end of the prefix, do a DFS to find all words
        def dfs(current_node, path):
            # If the current node marks end of a word, word can be added to results
            if current_node.is_end_of_word:
                results.append(path)

            # Recursively visit all children with updated path
            for char, child_node in current_node.children.items():
                dfs(child_node, path + char)
        
        # Start DFS from the end of the prefix
        dfs(node, prefix)

        # Print results or indicate no words found
        if print_result:
            if results:
                print("Words with prefix", prefix, ":", results)
            else:
                print("No words found with prefix", prefix)

    # Delete a word from the Trie    
    def delete(self, word):
        # Function for recursive deletion
        def recursive_delete(node, i):
            # Base case : if end of word is reached
            if i == len(word):
                node.is_end_of_word = False # Unmark the end of word
                return len(node.children) == 0 # If no children node can be deleted
            
            # Recursive case
            char = word[i] # Current character of the word

            # If character found in a child node, and this child can be deleted (no other words depend on it)
            if char in node.children and recursive_delete(node.children[char], i + 1):
                del node.children[char] # Delete the child node

                # Return True if current node can also be deleted
                return not node.is_end_of_word and len(node.children) == 0

            # If character not found or child can't be deleted, return False
            return False
        
        # Start recursive deletion from root and index 0 of the word
        recursive_delete(self.root, 0)