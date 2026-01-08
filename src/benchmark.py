import time
import tracemalloc
import os
import matplotlib.pyplot as plt

from trie import Trie
from patricia import PatriciaTrie

# Dataset sizes to test, need to match those generated in datasets.py
DATASETS = [100, 1000, 5000, 10000]

# Load words from dataset files
def load_words(size):
    with open(f"data/words_{size}.txt") as f:
        return [w.strip() for w in f.readlines()]

# Benchmark a data structure with given words
def benchmark_structure(structure, words):
    results = {} # Dictionary to store results

    # Measure insertion time and memory
    tracemalloc.start()
    start_time = time.perf_counter()
    for w in words:
        structure.insert(w)
    insert_time = time.perf_counter() - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    results["InsertTime"] = insert_time
    results["InsertMemory"] = peak

    # Measure search time
    start_time = time.perf_counter()
    for w in words:
        structure.search(w, False) # False to suppress printing
    results["SearchTime"] = time.perf_counter() - start_time

    # Measure range search time, with prefixes of length 3 from the first 100 words
    prefixes = [w[:3] for w in words[:100]]
    start_time = time.perf_counter()
    for p in prefixes:
        structure.range_search(p, False) # False to suppress printing
    results["RangeSearchTime"] = time.perf_counter() - start_time

    # Measure deletion time
    start_time = time.perf_counter()
    for w in words:
        structure.delete(w)
    results["DeleteTime"] = time.perf_counter() - start_time

    return results

# Run benchmarks and collect results
def run_benchmarks():
    all_results = [] # List to store all results

    # Iterate over all dataset sizes
    for size in DATASETS:
        # Load words for the current dataset size and initialize both structures
        words = load_words(size)
        trie = Trie()
        patricia = PatriciaTrie()

        # Benchmark both structures
        trie_res = benchmark_structure(trie, words)
        patricia_res = benchmark_structure(patricia, words)

        # Store results
        all_results.append((size, "Trie", trie_res))
        all_results.append((size, "PatriciaTrie", patricia_res))

    # Print results in a formatted table
    metrics = ["InsertTime","InsertMemory","SearchTime","RangeSearchTime","DeleteTime"]
    print(f"{'Size':>6} | {'Metric':<15} | {'Trie':>10} | {'Patricia':>10} | {'Diff %':>8}")
    print("-"*65)

    # For each dataset size, print the metrics and their differences
    for size in DATASETS:
        trie_res = next(r for s, t, r in all_results if s==size and t=="Trie")
        patricia_res = next(r for s, t, r in all_results if s==size and t=="PatriciaTrie")

        for metric in metrics:
            t_val = trie_res[metric]
            p_val = patricia_res[metric]
            diff = ((t_val - p_val)/t_val*100) if t_val != 0 else 0
            print(f"{size:6} | {metric:<15} | {t_val:10.6f} | {p_val:10.6f} | {diff:8.2f}")
        print("-"*65)

    # Plotting the results
    os.makedirs("results", exist_ok=True)
    plt.figure(figsize=(12, 8))

    # For each metric, create a subplot
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
    print("Graphs saved to results/performance.png")
    plt.show()

# Run benchmarks
if __name__ == "__main__":
    run_benchmarks()
