#!/usr/bin/env python3

def sum_equation(L):
    L = [0] if len(L) == 0 else L
    return " + ".join([str(x) for x in L]) + f" = {sum(L)}"

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
