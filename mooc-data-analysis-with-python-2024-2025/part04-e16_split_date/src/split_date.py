#!/usr/bin/env python3

import pandas as pd
import numpy as np

PATH = "src/Helsingin_pyorailijamaarat.csv"
DAY_MAP = {
        "ma": "Mon",
        "ti": "Tue",
        "ke": "Wed",
        "to": "Thu",
        "pe": "Fri",
        "la": "Sat",
        "su": "Sun"
    }

MONTH_MAP = {
    "tammi": "1",
    "helmi": "2",
    "maalis": "3",
    "huhti": "4",
    "touko": "5",
    "kesä": "6",
    "heinä": "7",
    "elo": "8",
    "syys": "9",
    "loka": "10",
    "marras": "11",
    "joulu": "12"
}

def split_date():
    df = pd.read_csv(PATH, sep=";")
    df.dropna(subset=['Päivämäärä'], inplace=True)
    columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    new_df = df["Päivämäärä"].str.split(' ', expand=True)
    new_df.columns = columns
    new_df.replace({"Weekday": DAY_MAP, "Month": MONTH_MAP}, inplace=True)
    new_df["Hour"] = new_df["Hour"].str[:2].astype(int)
    new_df[["Year", "Month", "Day"]] = new_df[["Year", "Month", "Day"]].astype(int)

    return new_df

def main():
    print(split_date())


if __name__ == "__main__":
    main()
