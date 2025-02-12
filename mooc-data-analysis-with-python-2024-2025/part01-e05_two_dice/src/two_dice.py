#!/usr/bin/env python3

def main():
    for dice1 in range(1, 6):
        for dice2 in range(1, 6):
            if dice1 + dice2 == 5:
                pair = (dice1, dice2)
                print(pair)

if __name__ == "__main__":
    main()
