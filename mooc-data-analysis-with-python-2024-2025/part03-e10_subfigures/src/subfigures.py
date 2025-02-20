#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    x = a[:,0]
    y = a[:, 1]
    c = a[:, 2]
    s = a[:, 3].astype(float)

    plt.subplot(1, 2, 1)
    plt.plot(x, y)

    plt.subplot(1, 2, 2)
    plt.scatter(x, y, c=c, s=s)

    plt.show()

def main():
    a = np.array([
        [1, 2, "red", 8],
        [2, 3, "blue", 4],
        [3, 5, "green", 12],
        [4, 9, "yellow", 25],
        [5, 6, "orange", 13],
        [6, 7, "pink", 7],
        [7, 7, "blue", 10],
        [8, 5, "yellow", 13],
        [9, 1, "pink", 20]
    ])
    subfigures(a)

if __name__ == "__main__":
    main()
