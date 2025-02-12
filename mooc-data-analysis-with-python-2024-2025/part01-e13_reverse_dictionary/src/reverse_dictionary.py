#!/usr/bin/env python3

def reverse_dictionary(d):
    reversed = {}
    for key in d.keys():
        english = key
        finnish_list = d[english]

        for finnish in finnish_list:
            english_list = reversed.get(finnish, [])
            english_list.append(english)
            reversed[finnish] = english_list
    return reversed

def main():
    d = {'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))
    pass

if __name__ == "__main__":
    main()
