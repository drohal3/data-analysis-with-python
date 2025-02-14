#!/usr/bin/env python3

def word_frequencies(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    counts = {}
    for line in lines:
        words = list(map(lambda x: x.strip("""!"#$%&'()*,-./:;?@[]_"""), line.split()))
        for word in words:
            counts[word] = counts.get(word, 0) + 1

    return counts

def main():
    frequencies = word_frequencies("src/alice.txt")
    for word in frequencies.keys():
        print(f"{word}\t{frequencies[word]}")

if __name__ == "__main__":
    main()
