#!/usr/bin/env python3

import pandas as pd
import numpy as np

PATH = "src/UK-top40-1964-1-2.tsv"

def last_week():
    df = pd.read_csv(PATH, sep="\t", header=0)
    df = df[~df['LW'].isin(["New", "Re"])]

    now_top_mask = df['Pos'].astype(int) == df['Peak Pos'].astype(int)
    not_kep_place_mask = df['Pos'].astype(int) != df['LW'].astype(int)
    df.loc[now_top_mask & not_kep_place_mask, 'Peak Pos'] = np.nan

    df['LW'], df['Pos'] = np.nan, df['LW'].astype(int)
    df['WoC'] = df['WoC'] - 1

    missing_values = np.setdiff1d(list(range(1, 41)), df['Pos'])
    df_missing = pd.DataFrame(missing_values, columns=['Pos'])
    df_missing['LW'] = np.nan
    df_missing['WoC'] = np.nan
    df_missing['Peak Pos'] = np.nan
    df_missing['Publisher'] = None
    df_missing['Artist'] = None
    df_missing['Title'] = None

    df = pd.concat([df, df_missing])
    df = df.sort_values(by='Pos')
    df.index = range(0, len(df))

    return df

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
