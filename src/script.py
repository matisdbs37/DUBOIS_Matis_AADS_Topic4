from trie import Trie
from patricia import PatriciaTrie
from visualize import visualize_trie

print("------ Visualizing Trie operations ------\n")

t = Trie()

print("Inserting 'test' and 'team' into Trie")
t.insert("test")
t.insert("team")
visualize_trie(t, "results/trie_step1")
print("Result available at results/trie_step1.pdf\n")

print("Inserting 'hello' into Trie")
t.insert("hello")
visualize_trie(t, "results/trie_step2")
print("Result available at results/trie_step2.pdf\n")

print("Searching and range searching in Trie")
t.search("test")
t.search("tes")
t.search("cat")
t.range_search("te")
t.range_search("b")

print("\nDeleting 'test' from Trie, and try to delete 'ello' (not present)")
t.delete("test")
t.delete("ello")
visualize_trie(t, "results/trie_step3")
print("Result available at results/trie_step3.pdf\n")

print("------ Visualizing Patricia Trie operations ------\n")

p = PatriciaTrie()

print("Inserting 'test' and 'team' into Patricia Trie")
p.insert("test")
p.insert("team")
visualize_trie(p, "results/patricia_step1")
print("Result available at results/patricia_step1.pdf\n")

print("Inserting 'hello' into Patricia Trie")
p.insert("hello")
visualize_trie(p, "results/patricia_step2")
print("Result available at results/patricia_step2.pdf\n")

print("Searching and range searching in Patricia Trie")
p.search("test")
p.search("tes")
p.search("cat")
p.range_search("te")
p.range_search("b")

print("\nDeleting 'test' from Patricia Trie, and try to delete 'ello' (not present)")
p.delete("test")
p.delete("ello")
visualize_trie(p, "results/patricia_step3")
print("Result available at results/patricia_step3.pdf\n")