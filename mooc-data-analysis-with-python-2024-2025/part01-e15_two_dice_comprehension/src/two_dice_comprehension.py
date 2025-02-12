#!/usr/bin/env python3

def main():
     # NOTE: example solution provides better answer:
     # print("\n".join(f"({a},{b})" for a in range(1, 7) for b in range(1, 7) if a + b == 5))
     combinations = [(dice1,dice2) for dice1 in range(1,6) for dice2 in range(1,6) if dice1 + dice2 == 5]
     for combination in combinations:
         print(combination)

if __name__ == "__main__":
    main()
