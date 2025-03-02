#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    municipalities = df.loc["Akaa":"Äänekoski"]
    columns = [
        "Population",
        "Share of Swedish-speakers of the population, %",
        "Share of foreign citizens of the population, %"
    ]
    municipalities = municipalities[columns]
    municipalities = municipalities[
        (municipalities["Share of Swedish-speakers of the population, %"] > 5.0)
        & (municipalities["Share of foreign citizens of the population, %"] > 5.0)
    ]
    return municipalities

def main():
    print(swedish_and_foreigners())


if __name__ == "__main__":
    main()
