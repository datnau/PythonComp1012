#DatNguyenA1Q1.py
#
# Course: COMP 1012
# Instructor: Abolfazl Babaei
# Assignment: 1 Question 1
# Author: Thanh Dat Nguyen
# Version: 2023/10/14
#
# Purpose: calculate the GCD and the LCM
#
# var1 - the use / meaning of each variable in the program

from time import ctime
print('\n--------------------------------------------------\n')

def gcd_lcm(m, n):
    p = m * n
    while m != n:
        if m < n:
            n = n - m
        else:
            m = m - n
    return m, p // m

m_input = input("Enter the first number: ")
n_input = input("Enter the second number: ")

if m_input.isnumeric() and n_input.isnumeric():
    m = int(m_input)
    n = int(n_input)

    gcd, lcm = gcd_lcm(m, n)

    print("The Greatest Common Divider is:", gcd)
    print("The Least Common Multiple is:", lcm)

else:
    print("A float value is entered which is not acceptable!")

print("""
Programmed by Thanh Dat Nguyen
Date: %s
End of pro
cessing.""" % ctime())
