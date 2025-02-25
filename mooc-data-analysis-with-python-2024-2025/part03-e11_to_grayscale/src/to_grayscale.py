#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(a):
    return np.average(a, axis=-1, weights=np.array([0.2126, 0.7152, 0.0722]))

def to_red(a):
    return a * (1, 0, 0)

def to_green(a):
    return a * (0, 1, 0)

def to_blue(a):
    return a * (0, 0, 1)

def main():
    path: str = "./src/painting.png"
    image = plt.imread(path).copy()

    plt.subplot(3, 1, 1)
    plt.imshow(to_red(image))

    plt.subplot(3, 1, 2)
    plt.imshow(to_green(image))

    plt.subplot(3, 1, 3)
    plt.imshow(to_blue(image))
    plt.show()

if __name__ == "__main__":
    main()
