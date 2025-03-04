#!/usr/bin/env python3

import pandas as pd

PATH = "src/Helsingin_pyorailijamaarat.csv"
def cyclists():
    return pd.read_csv(PATH, sep=";").dropna(axis=1, how="all").dropna(axis=0, how="all")


def main():
    print(cyclists())


if __name__ == "__main__":
    main()
