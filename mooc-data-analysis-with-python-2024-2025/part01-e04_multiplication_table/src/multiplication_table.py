#!/usr/bin/env python3


def main():
    for multiplicand in range(1, 11):
        for multiplier in range(1, 11):
            product = multiplicand * multiplier
            print(f"{product:>4}", end="")
        print("") # new line

if __name__ == "__main__":
    main()
