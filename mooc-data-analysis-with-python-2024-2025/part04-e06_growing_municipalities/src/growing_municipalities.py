#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    all_count = len(df)
    growing_count = len(df[df["Population change from the previous year, %"] > 0])
    return float(growing_count) / float(all_count)

def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    municipalities = df.loc["Akaa":"Äänekoski"]
    proportion = growing_municipalities(municipalities)
    print(f"Proportion of growing municipalities: {proportion * 100:.1f}%")


if __name__ == "__main__":
    main()
