from trie import Trie
from patricia import PatriciaTrie
from visualize import visualize_trie

t = Trie()
t.insert("test")
t.insert("team")
visualize_trie(t, "results/trie_step1")
t.insert("hello")
visualize_trie(t, "results/trie_step2")
t.search("test")
t.search("aaah")
visualize_trie(t, "results/trie_step3")
t.delete("test")
visualize_trie(t, "results/trie_step4")

p = PatriciaTrie()
p.insert("test")
p.insert("team")
visualize_trie(p, "results/patricia_step1")
p.insert("hello")
visualize_trie(p, "results/patricia_step2")
p.search("test")
p.search("aaah")
visualize_trie(p, "results/patricia_step3")
p.delete("test")
visualize_trie(p, "results/patricia_step4")
