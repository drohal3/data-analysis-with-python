#!/usr/bin/env python3

def triple(n):
    return n * 3

def square(n):
    return n ** 2

def main():
    for number in range(1, 10):
        triple_result = triple(number)
        square_result = square(number)
        if square_result > triple_result:
            break
        print(f"triple({number})=={triple_result} square({number})=={square_result}")

if __name__ == "__main__":
    main()
