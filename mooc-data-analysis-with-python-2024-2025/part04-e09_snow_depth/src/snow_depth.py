#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    snow_depth_c = df["Snow depth (cm)"]
    return snow_depth_c.max()

def main():
    d = snow_depth()
    print(f"Max snow depth: {d:.1f}")


if __name__ == "__main__":
    main()
