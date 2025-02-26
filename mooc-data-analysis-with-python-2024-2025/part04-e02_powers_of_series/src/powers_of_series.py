#!/usr/bin/env python3

import pandas as pd

def powers_of_series(s, k):
    df = pd.DataFrame()
    for column in range(k):
        power = column + 1
        df[power] = s**power

    return df
    
def main():
    s = pd.Series([1, 2, 3, 4, 5], index=list("abcde"))
    print(powers_of_series(s, 5))


if __name__ == "__main__":
    main()
