#DatNguyenA2Q3.py
#
# Course: COMP 1012
# Instructor: Abolfazl Babaei
# Assignment: 2 Question 3
# Author: Thanh Dat Nguyen
# Version: 2023/10/31
#
# Purpose: Compute the approximate area of a heart using lists and time the computation.
# var1 - the use / meaning of each variable in the program
from time import ctime
print('\n--------------------------------------------------\n')

from math import factorial

def PasTri(n):
    for i in range(n):
        values = [factorial(i) // (factorial(j) * factorial(i - j)) for j in range(i + 1)]
        print(values)

PasTri(6)


print("""
Programmed by Thanh Dat Nguyen
Date: %s
End of processing.""" % ctime())