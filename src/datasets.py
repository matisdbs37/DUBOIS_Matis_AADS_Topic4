import random
import string
import os

# Generate n unique random words of given length
def generate_words(n, length=8):
    words = set() # Set to avoid duplicates
    while len(words) < n:
        # Create a random word made of lowercase letters
        words.add("".join(random.choices(string.ascii_lowercase, k=length)))
    return list(words)

# Create the data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Different dataset sizes to generate
sizes = [100, 1000, 5000, 10000]

# Generate a file containing random words for each dataset size and save them in data directory
for size in sizes:
    words = generate_words(size)
    with open(f"data/words_{size}.txt", "w") as f:
        for word in words:
            f.write(word + "\n")