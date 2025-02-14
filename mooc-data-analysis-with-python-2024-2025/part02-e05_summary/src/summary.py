#!/usr/bin/env python3
import math
import sys

def summary(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    numbers = []
    for number in lines:
        try:
            f = float(number)
        except ValueError:
            continue
        numbers.append(f)
    total = sum(numbers)
    mean = total / len(numbers)
    partial = [(x - mean) ** 2 for x in numbers]
    stddev = math.sqrt(sum(partial) / (len(partial) - 1))

    return (total, mean, stddev)

def main():
    for file in sys.argv[1:]:
        triple = summary(file)
        print(f"File: {file} Sum: {triple[0]:.6f} Average: {triple[1]:.6f} Stddev: {triple[2]:.6f}")
    pass

if __name__ == "__main__":
    main()
