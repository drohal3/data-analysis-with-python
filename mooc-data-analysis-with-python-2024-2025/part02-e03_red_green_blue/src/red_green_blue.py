#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    with open(filename, "r") as f:
        lines = f.readlines()[1:]

    transformed = []
    for line in lines:
        m = re.search(r"(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})\s+(.+)", line)
        red,green,blue,name = m.groups()
        transformed.append(f"{red}\t{green}\t{blue}\t{name}")
    return transformed


def main():
    print(red_green_blue())

if __name__ == "__main__":
    main()
