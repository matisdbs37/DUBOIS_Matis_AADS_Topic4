import time
import tracemalloc
import os
import matplotlib.pyplot as plt

from trie import Trie
from patricia import PatriciaTrie

DATASETS = [100, 1000, 5000, 10000]

def load_words(size):
    with open(f"data/words_{size}.txt") as f:
        return [w.strip() for w in f.readlines()]

def benchmark_structure(structure, words):
    results = {}

    # INSERT
    tracemalloc.start()
    start_time = time.perf_counter()
    for w in words:
        structure.insert(w)
    insert_time = time.perf_counter() - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    results["InsertTime"] = insert_time
    results["InsertMemory"] = peak

    # SEARCH
    start_time = time.perf_counter()
    for w in words:
        structure.search(w)
    results["SearchTime"] = time.perf_counter() - start_time

    # RANGE SEARCH
    prefixes = [w[:3] for w in words[:100]]
    start_time = time.perf_counter()
    for p in prefixes:
        structure.range_search(p)
    results["RangeSearchTime"] = time.perf_counter() - start_time

    # DELETE
    start_time = time.perf_counter()
    for w in words:
        structure.delete(w)
    results["DeleteTime"] = time.perf_counter() - start_time

    return results

def run_benchmarks():
    all_results = []

    for size in DATASETS:
        words = load_words(size)
        trie = Trie()
        patricia = PatriciaTrie()

        trie_res = benchmark_structure(trie, words)
        patricia_res = benchmark_structure(patricia, words)

        all_results.append((size, "Trie", trie_res))
        all_results.append((size, "PatriciaTrie", patricia_res))

    # Affichage lisible + différences
    metrics = ["InsertTime","InsertMemory","SearchTime","RangeSearchTime","DeleteTime"]
    print(f"{'Size':>6} | {'Metric':<15} | {'Trie':>10} | {'Patricia':>10} | {'Diff %':>8}")
    print("-"*65)

    for size in DATASETS:
        trie_res = next(r for s, t, r in all_results if s==size and t=="Trie")
        patricia_res = next(r for s, t, r in all_results if s==size and t=="PatriciaTrie")

        for metric in metrics:
            t_val = trie_res[metric]
            p_val = patricia_res[metric]
            diff = ((t_val - p_val)/t_val*100) if t_val != 0 else 0
            print(f"{size:6} | {metric:<15} | {t_val:10.6f} | {p_val:10.6f} | {diff:8.2f}")
        print("-"*65)

    # ----------- Génération du graphe ------------
    os.makedirs("results", exist_ok=True)
    plt.figure(figsize=(12, 8))

    for i, metric in enumerate(metrics):
        plt.subplot(3, 2, i+1)
        trie_vals = [next(r for s, t, r in all_results if s==size and t=="Trie")[metric] for size in DATASETS]
        pat_vals = [next(r for s, t, r in all_results if s==size and t=="PatriciaTrie")[metric] for size in DATASETS]

        plt.plot(DATASETS, trie_vals, marker='o', label='Trie')
        plt.plot(DATASETS, pat_vals, marker='s', label='PatriciaTrie')

        plt.title(metric)
        plt.xlabel("Dataset size")
        plt.ylabel(metric)
        plt.legend()
        plt.grid(True)

    plt.tight_layout()
    plt.savefig("results/performance.png")
    print("Graphe sauvegardé dans results/performance.png")
    plt.show()

if __name__ == "__main__":
    run_benchmarks()
