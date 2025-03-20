#!/usr/bin/env python3

import pandas as pd

def top_bands():
    bands = pd.read_csv("src/bands.tsv", sep="\t")
    top40 = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")

    bands["Band"] = bands["Band"].str.upper()
    top40["Artist"] = top40["Artist"].str.upper()

    return pd.merge(bands, top40, left_on="Band", right_on="Artist")

def main():
    print(top_bands().head())


if __name__ == "__main__":
    main()
