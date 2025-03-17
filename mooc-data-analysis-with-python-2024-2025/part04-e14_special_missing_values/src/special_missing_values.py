#!/usr/bin/env python3

import pandas as pd
import numpy as np
PATH = "src/UK-top40-1964-1-2.tsv"
def special_missing_values():
    # example solution:
    # df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    # m = (df["LW"] == "New") | (df["LW"] == "Re")
    # df.loc[m, "LW"] = np.nan
    # df["LW"] = pd.to_numeric(df["LW"])
    # m2 = df["LW"] < df["Pos"]
    # return df[m2]
    df = pd.read_csv(PATH, sep="\t")
    df["LW"] = df["LW"].replace(("New", "Re"), np.nan)
    not_na = df[df["LW"].notna()]
    filtered = not_na[not_na["Pos"].astype(int) > not_na["LW"].astype(int)]

    return filtered

def main():
    print(special_missing_values())


if __name__ == "__main__":
    main()
