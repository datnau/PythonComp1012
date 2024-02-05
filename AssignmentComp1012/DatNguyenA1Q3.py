#DatNguyenA1Q3.py
#
# Course: COMP 1012
# Instructor: Abolfazl Babaei
# Assignment: 1 Question 3
# Author: Thanh Dat Nguyen
# Version: 2023/10/14
#
# Purpose: calculate the approximate value of e^-x^2
#
# var1 - the use / meaning of each variable in the program

from time import ctime
import math

print('\n--------------------------------------------------\n')

def calculate(DecimalPlaces, x):
    term1 = 0
    n = 1
    eee = 1
    count = 0

    while True:
        terms = x ** (2 * term1) / eee
        term1 += 1
        eee *= term1
        count += n * terms
        n *= -1
        if terms < 10 ** (-DecimalPlaces):
            break

    return count, term1

def main():
    print("Calculate e^(-x^2) given the number of decimal places and the value of x")

    DecimalPlaces = int(input("\nEnter the number of decimal places: "))
    x = int(input("\nEnter the value of x: "))

    result, term1 = calculate(DecimalPlaces, x)

    print("\nPython's values of e^%d is:" % (-2 * x))
    print('%.15f' % math.exp(-(x ** 2)))
    print("\nThe approximate value of e^%d is:" % (-2 * x))
    print(('%.' + str(DecimalPlaces) + 'f') % result)
    print("\nThe number of terms in the series is %d" % term1)

if __name__ == "__main__":
    main()

print("""
Programmed by Thanh Dat Nguyen
Date: %s
End of processing.""" % ctime())
