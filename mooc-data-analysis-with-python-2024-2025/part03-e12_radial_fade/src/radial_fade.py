#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import math

def center(a):
    return (a.shape[0] - 1) / 2, (a.shape[1] - 1) / 2   # note the order: (center_y, center_x)

def radial_distance(a):
    height = a.shape[0]
    width = a.shape[1]
    c = center(a)
    m = [[math.sqrt((c[0] - y)**2 + (c[1] - x)**2) for x in range(width)] for y in range(height)]
    return np.array(m)


def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    return np.interp(a, (a.min(), a.max()), (tmin, tmax))

def radial_mask(a):
    return scale(1 - radial_distance(a))

def radial_fade(a):
    mask = radial_mask(a)
    mask3d = mask[:, :, np.newaxis]
    return a * mask3d

def main():
    path: str = "./src/painting.png"
    image = plt.imread(path)

    plt.subplot(3, 1, 1)
    plt.imshow(image)

    plt.subplot(3, 1, 2)
    plt.imshow(radial_mask(image))

    plt.subplot(3, 1, 3)
    plt.imshow(radial_fade(image))
    plt.show()


if __name__ == "__main__":
    main()
