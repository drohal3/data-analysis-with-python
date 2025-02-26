#!/usr/bin/env python3

import pandas as pd

def main():
    path = "src/municipal.tsv"
    data = pd.read_csv(path, sep="\t")
    shape = data.shape
    print(f"Shape: {shape[0]},{shape[1]}")
    # Note better solution for Shape: print("Shape: {}, {}".format(*df.shape))
    print("Columns:")
    columns = data.columns
    for column in columns:
        print(column)


if __name__ == "__main__":
    main()
