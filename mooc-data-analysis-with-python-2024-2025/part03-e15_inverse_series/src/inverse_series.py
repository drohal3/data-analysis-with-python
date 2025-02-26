#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    # Note: the following should be enough
    # return pd.Series(s.index, s.values)
    return pd.Series(s.index.tolist(), index=s.values.tolist())

def main():
    d = {2001: "Bush", 2005: "Bush", 2009: "Obama", 2013: "Obama", 2017: "Trump"}
    original = pd.Series(d, name="Presidents")
    print("original:\n", original)
    inverse = inverse_series(original)
    print("inverse:\n", inverse)


if __name__ == "__main__":
    main()
