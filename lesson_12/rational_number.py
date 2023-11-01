import math

class Rational:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __str__(self):
        return f"{self.__numerator} / {self.__denominator}"

    def __mul__(self, other):
        n_numerator = self.__numerator * other.__numerator
        n_denominator = self.__denominator * other.__denominator
        return Rational(n_numerator, n_denominator)

    def __truediv__(self, other):
        n_numerator = self.__numerator * other.__denominator
        n_denominator = self.__denominator * other.__numerator
        return Rational(n_numerator, n_denominator)

    def __add__(self, other):
        n_denominator = self.__denominator * other.__denominator
        n_numerator = self.__numerator * other.__denominator + other.__numerator * self.__denominator
        return Rational(n_numerator, n_denominator)

    def __sub__(self, other):
        n_denominator = self.__denominator * other.__denominator
        n_numerator = self.__numerator * other.__denominator - other.__numerator * self.__denominator
        return Rational(n_numerator, n_denominator)

    def __eq__(self, other):
        return self.__numerator == other.__numerator and self.__denominator == other.__denominator

    def __gt__(self, other):
        return self.__numerator * other.__denominator > other.__numerator * self.__denominator

    def __lt__(self, other):
        return self.__numerator * other.__denominator < other.__numerator * self.__denominator


if __name__ == '__main__':
    x1 = Rational(1, 4)
    x2 = Rational(2, 5)

    print(x1)
    print(x2)

    f_mul = x1 * x2
    print(f_mul)

    f_div = x1 / x2
    print(f_div)
