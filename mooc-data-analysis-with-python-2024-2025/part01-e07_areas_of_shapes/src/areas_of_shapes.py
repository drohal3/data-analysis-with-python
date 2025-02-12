#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    def triangle():
        base = input("Give base of the triangle: ")
        height = input("Give height of the triangle: ")
        area = float(base) * float(height) / 2
        print(f"The area is {area:.6f}")

    def rectangle():
        width = input("Give width of the rectangle: ")
        height = input("Give height of the rectangle: ")
        area = float(width) * float(height)
        print(f"The area is {area:.6f}")

    def circle():
        radius = input("Give radius of the circle: ")
        area = math.pi * float(radius) ** 2
        print(f"The area is {area:.6f}")

    def prompt():
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "triangle":
            triangle()
        elif shape == "rectangle":
            rectangle()
        elif shape == "circle":
            circle()
        elif shape == "":
            return
        else:
            print("Unknown shape!")
        prompt()

    prompt()




if __name__ == "__main__":
    main()
