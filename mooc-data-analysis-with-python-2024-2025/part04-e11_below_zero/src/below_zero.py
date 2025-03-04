#!/usr/bin/env python3

import pandas as pd

def below_zero():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    # alternative solution:
    # return sum(df["Air temperature (degC)"] < 0.0)
    filtered = df[df["Air temperature (degC)"] < 0]
    return len(filtered)

def main():
    n = below_zero()
    print(f"Number of days below zero: {n}")


if __name__ == "__main__":
    main()
