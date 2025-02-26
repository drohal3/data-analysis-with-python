#!/usr/bin/env python3
import numpy as np
import pandas as pd


def cities():
    raw = ["Helsinki         643272     715.48",
           "Espoo            279044     528.03",
           "Tampere          231853     689.59",
           "Vantaa           223027     240.35",
           "Oulu             201810     3817.52"]
    columns = ["Population", "Total area"]

    data = np.array([[parts[0], int(parts[1]), float(parts[2])] for line in raw for parts in [line.split(maxsplit=2)]])
    indexes = data[:, 0]
    values = data[:, 1:].astype(float)

    return pd.DataFrame(values, index=indexes, columns=columns)


def main():
    print(cities())


if __name__ == "__main__":
    main()
