# Performance comparison of a Trie and a Patricia Trie

This project compares the performance (time and memory) of a Prefix Trie and a Patricia Trie.

## Setup

First, clone the repository :

```bash
git clone https://github.com/matisdbs37/DUBOIS_Matis_AADS_Topic4.git
cd DUBOIS_Matis_AADS_Topic4
```

Then, initialize the virtual environment :

For **Windows** :

```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

For **Linux** :

```bash
python3 -m venv venv
source venv/bin/activate
```

Once you are in the virtual environment, you can download the dependencies :

```bash
pip install -r requirements.txt
```

You also need to install Graphviz on your device :

For **Linux** :

```bash
sudo apt install graphviz
```

For **Windows**, you can use this link : https://graphviz.org/download/

## Datasets

Datasets are generated with the **src/datasets.py** file.

When this file is run, four datasets are created in the data folder (100, 500, 1000, and 10000 words). The datasets are already available in this folder.

Since the words are generated randomly, you can run **src/datasets.py** again to get new words in datasets.

## Data Structures and Test Script

The implementations of the classes for Trie and Patricia Trie are available in **src/trie.py** and **src/patricia.py**. An implementation for their visualization is also available in **src/visualize.py**.

In **src/script.py**, a small script is available that allows you to test all the operations of the Trie and Patricia Trie. Running this script tests insertion, search, range search, and deletion.

A sample test is already included in this file, but you can change it to perform other tests if you wish.

You can view the state of a Trie at any time using `visualize_trie` by specifying the Trie and a filename. The visualization will then be available in the provided file (if possible, place it in the `results` folder).

For example :

```python
t = Trie()
t.insert("test")
visualize_trie(t, "results/trie")
```
And the visualization is available in results/trie.pdf. Use the existing script as a guide if you want to conduct further tests.

## Benchmark

All benchmark experiments are available in **src/benchmark.py**.

By running this file, you will obtain a comparison between the Trie and the Patricia Trie across different metrics directly in the console, and a performance graph will then be generated in **results/performance.png**.