#!/usr/bin/env python3

class Prepend(object):
    def __init__(self, pre):
        self.pre = pre

    def write(self, txt):
        print(self.pre + txt)

def main():
    p = Prepend("+++ ")
    p.write("Hello")

if __name__ == "__main__":
    main()
