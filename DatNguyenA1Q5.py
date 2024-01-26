#DatNguyenA1Q5.py
#
# Course: COMP 1012
# Instructor: Abolfazl Babaei
# Assignment: 1 Question 5
# Author: Thanh Dat Nguyen
# Version: 2023/10/31
#
# Purpose: 
# var1 - the use / meaning of each variable in the program

from time import ctime
print('\n--------------------------------------------------\n')

numerator = int(input("Enter the numerator: "))
denominator = int(input("\nEnter the denominator: "))
position = int(input("\nEnter the position of the decimal digit that you want: "))

result = numerator / denominator
remainder = numerator % denominator

digits_after_decimal = []
for i in range(position):
    remainder *= 10
    digit = remainder // denominator
    digits_after_decimal.append(digit)
    remainder %= denominator

# Print the result and the digit at the specified position
print("\nThe answer of the division is: %.11f" % result)
print("\n%d is placed in position %d after the decimal point." % (digits_after_decimal[position - 1], position))

print("""
Programmed by Thanh Dat Nguyen
Date: %s
End of processing.""" % ctime())