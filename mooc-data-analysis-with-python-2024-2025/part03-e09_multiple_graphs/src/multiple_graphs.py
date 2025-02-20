#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def main():
    plt.plot([2,4,6,7], [4,3,5,1], label="first line", color="blue")
    plt.plot([1,2,3,4], [4,2,3,1], label="second line", color="red")

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Multiple Graphs in Single Plot")
    plt.legend()  # Show legend
    plt.show()

if __name__ == "__main__":
    main()
