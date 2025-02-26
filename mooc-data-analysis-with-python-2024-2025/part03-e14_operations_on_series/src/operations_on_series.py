#!/usr/bin/env python3
import pandas as pd

def create_series(L1, L2):
    indices = ["a", "b", "c"]
    return pd.Series(L1, index=indices), pd.Series(L2, index=indices)
    
def modify_series(s1, s2):
    s1["d"] = s2["b"]
    del s2["b"]

    return s1, s2

def main():
    L1 = ["s1a", "s1b", "s1c"]
    L2 = ["s2a", "s2b", "s2c"]

    s1, s2 = create_series(L1, L2)

    s1, s2 = modify_series(s1, s2)
    print(s1 + s2)

    
if __name__ == "__main__":
    main()
