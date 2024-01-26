#DatNguyenA2Q2.py
#
# Course: COMP 1012
# Instructor: Abolfazl Babaei
# Assignment: 2 Question 2
# Author: Thanh Dat Nguyen
# Version: 2023/10/31
#
# Purpose: 
# var1 - the use / meaning of each variable in the program
from time import ctime
print('\n--------------------------------------------------\n')


import math

def grablist():
    list_size = int(input("Enter the length of the list: "))
    user_list = []
    for i in range(list_size):
        element = float(input("Enter element %d: " % (i + 1)))
        user_list.append(element)

    print("Sample data: %s" % user_list)
    sd_calc(user_list)

def avg_calc(user_list):
    avg = sum(user_list) / len(user_list)
    return avg

def sd_calc(user_list):
    avg = avg_calc(user_list)
    element2 = [(element - avg) for element in user_list]
    element3 = [i**2 for i in element2]
    avg2 = sum(element3) / len(element3)
    sd = math.sqrt(avg2)
    print("Standard Deviation: %s" % sd)

grablist()


print("""
Programmed by Thanh Dat Nguyen
Date: %s
End of processing.""" % ctime())