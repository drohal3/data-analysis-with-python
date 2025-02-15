#!/usr/bin/env python3

import sys
from functools import reduce

def file_count(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    return reduce(lambda acc, x: (acc[0] + 1, acc[1] + len(x.split()), acc[2] + len(x)), lines, (0,0,0))

def main():
    for file in sys.argv[1:]:
        triple = file_count(file)
        print(f"{triple[0]}\t{triple[1]}\t{triple[2]}\t{file}")

if __name__ == "__main__":
    main()
