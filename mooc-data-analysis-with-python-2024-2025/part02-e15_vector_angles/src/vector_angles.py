#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    product = np.sum(X * Y, axis=1)
    X_magnitude = np.sqrt(np.sum(X**2, axis=1))
    Y_magnitude = np.sqrt(np.sum(Y**2, axis=1))
    q = np.arccos(np.clip(product / (X_magnitude * Y_magnitude), -1, 1))
    return np.degrees(q)

def main():
    a = np.array([[0, 0, 1], [-1, 1, 0]])
    b = np.array([[0, 1, 0], [1, 1, 0]])
    print(vector_angles(a, b))

if __name__ == "__main__":
    main()
