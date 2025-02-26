#!/usr/bin/env python3
import pandas as pd

def read_series():
    series = pd.Series()
    while True:
        line = input("Enter an index separated by a space: ")
        if line == "":
            break

        line_split = line.split()
        if len(line_split) != 2:
            raise ValueError("Invalid input: expected 2 words separated by a space!")
        key = line_split[0]
        value = line_split[1]
        series[key] = value

    return series

def main():
    series = read_series()
    print(series.head())


if __name__ == "__main__":
    main()
