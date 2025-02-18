#!/usr/bin/env python3

class Rational(object):
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError(f"denominator can't be {denominator}")
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        return Rational((self.numerator * other.denominator) + (other.numerator * self.denominator),self.denominator * other.denominator)

    def __sub__(self, other):
        return Rational((self.numerator * other.denominator) - (other.numerator * self.denominator),self.denominator * other.denominator)

    def __mul__(self, other):
        return Rational(self.numerator * other.numerator,self.denominator * other.denominator)

    def __truediv__(self, other):
        return Rational(self.numerator * other.denominator,other.numerator * self.denominator)

    def __eq__(self, other):
        return self.numerator / self.denominator == other.numerator / other.denominator

    def __gt__(self, other):
        return self.numerator / self.denominator > other.numerator / other.denominator

    def __lt__(self, other):
        return self.numerator / self.denominator < other.numerator / other.denominator

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
