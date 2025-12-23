import random
import string
import os

def generate_words(n, length=8):
    words = set()
    while len(words) < n:
        words.add("".join(random.choices(string.ascii_lowercase, k=length)))
    return list(words)

os.makedirs("data", exist_ok=True)

sizes = [100, 1000, 5000, 10000]

for size in sizes:
    words = generate_words(size)
    with open(f"data/words_{size}.txt", "w") as f:
        for word in words:
            f.write(word + "\n")