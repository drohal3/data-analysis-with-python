#!/usr/bin/env python3
import numpy as np
from functools import reduce


def matrix_power(a, n):
    if n >= 0:
        return reduce(lambda x, y: x @ y, (a for _ in range(n)), np.eye(a.shape[0]))
    else:
        return np.linalg.inv(matrix_power(a, n * -1))

def main():
    return

if __name__ == "__main__":
    main()
