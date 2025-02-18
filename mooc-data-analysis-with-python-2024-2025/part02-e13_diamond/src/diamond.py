#!/usr/bin/env python3

import numpy as np

def diamond(n):
    # better solution:
    #   e = np.eye(n, dtype=int)
    #   a = np.concatenate([e[::-1], e[:, 1:]], axis=1)
    #   result = np.concatenate([a[:-1], a[::-1]], axis=0)
    #   return result
    eye = np.eye(n,n, k=0, dtype=int),
    eye_mirror = eye[0][:,::-1]
    top = np.concatenate((eye_mirror[:,:-1],eye[0]),axis=1)
    top_mirror = top[::-1,:]
    bottom = top_mirror[1:,:]
    return np.concatenate((top,bottom))

def main():
    print(diamond(5))

if __name__ == "__main__":
    main()
