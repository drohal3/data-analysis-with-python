#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    # better solution: return np.split(a, a.shape[0], axis=0)
    return [row.reshape(1, len(a.T)) for row in a]

def get_column_vectors(a):
    # better solution: return np.split(a, a.shape[1], axis=1)
    return [col.reshape(len(a), 1) for col in a.T]

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
