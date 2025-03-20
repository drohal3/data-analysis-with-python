#!/usr/bin/env python3

import pandas as pd
import numpy as np

PATH = "src/presidents.tsv"

STR_NUM = {

}

def cleaning_data():
    def clean_names(names):
        names = names.str.split(",")
        names = names.apply(lambda x: ' '.join(x[::-1]).strip())
        names = names.str.title()
        return names

    df = pd.read_csv(PATH, sep="\t")
    df["President"] = clean_names(df["President"])
    df["Vice-president"] = clean_names(df["Vice-president"])
    df["Start"] = df["Start"].str[:4]
    df.replace({"Last": {"-": np.nan}, "Seasons": {"two": "2"}}, inplace=True)
    df = df.astype({"President": object, "Start": int, "Last": float, "Seasons": int, "Vice-president": object})
    return df


def main():
    print(cleaning_data())


if __name__ == "__main__":
    main()
