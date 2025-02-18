#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    return np.sqrt(np.sum(a**2, axis=1))

def main():
    a = np.arange(16).reshape(4,4)
    print(vector_lengths(a))

if __name__ == "__main__":
    main()
