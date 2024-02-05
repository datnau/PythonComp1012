#DatNguyenA1Q4.py
#
# Course: COMP 1012
# Instructor: Abolfazl Babaei
# Assignment: 1 Question 4
# Author: Thanh Dat Nguyen
# Version: 2023/10/14
#
# Purpose: write a piece of code in python that grabs N in the input and print out the N 
# var1 - the use / meaning of each variable in the program

from time import ctime
print('\n--------------------------------------------------\n')

n = int(input("Enter the number of the desired terms: "))

for i in range(1,n+1):
    temp = 1
    print(temp,end="")
    
    for j in range(1,i):
        temp = temp + 4 + 3*(j-1)
        print("",temp,end="")
    print()
    
print("""
Programmed by Thanh Dat Nguyen
Date: %s
End of processing.""" % ctime())