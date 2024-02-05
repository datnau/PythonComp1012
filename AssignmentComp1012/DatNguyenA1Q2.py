#DatNguyenA1Q2.py
#
# Course: COMP 1012
# Instructor: Abolfazl Babaei
# Assignment: 1 Question 2
# Author: Thanh Dat Nguyen
# Version: 2023/10/14
#
# Purpose: calculate the three cubic roots of a complex number
#
# var1 - the use / meaning of each variable in the program

from time import ctime
print('\n--------------------------------------------------\n')

from math import atan, cos, sin, pi, sqrt

a = float(input("Enter the real part of the complex number: "))
print("\n")
b = float(input("Enter the imaginary part of the complex number: "))
print("\n")
if a == 0:
    print("Error: The real part (a) cannot be zero.")
else:
    c = complex(a, b)
    print("The complex number is", c)
    print("\n")
    r = sqrt(a**2 + b**2) 
    theta = atan(b / a)  


    roots = []
    for k in range(3):
        root = (r ** (1/3)) * (cos((2 * pi * k + theta) / 3) + 1j * sin((2 * pi * k + theta) / 3))
        roots.append(root)

    print("root1 =", roots[0])
    print("root1^3 =", roots[0] ** 3)
    print("\n")
    print("root2 =", roots[1])
    print("root2^3 =", roots[1] ** 3)
    print("\n")
    print("root3 =", roots[2])
    print("root3^3 =", roots[2] ** 3)

print("""
Programmed by Thanh Dat Nguyen
Date: %s
End of processing.""" % ctime())