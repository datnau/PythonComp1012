#DatNguyenA4Q1.py
#
# Course: COMP 1012
# Instructor: Abolfazl Babaei
# Assignment: 4 Question 1
# Author: Thanh Dat Nguyen
# Version: 2023/12/10
#
# Purpose: 
import numpy as np
from time import ctime
def getPosInt(prompt):
    while True:
        try:
            user_input = input(prompt)
            if not user_input:
                raise ValueError("Missing input!")

            pos_int = int(user_input)
            if pos_int <= 0:
                raise ValueError("%d is not greater than 0!" % pos_int)

            return pos_int

        except ValueError as ve:
            print(ve)

def getBoundedInt(prompt, lowerBound, upperBound):
    while True:
        try:
            user_input = input(prompt)
            if not user_input:
                raise ValueError("Missing input!")

            bounded_int = int(user_input)
            if not (lowerBound <= bounded_int <= upperBound):
                raise ValueError("%d is not between %d and %d!" % (bounded_int, lowerBound, upperBound))

            return bounded_int

        except ValueError as ve:
            print(ve)

def addTrashToCan(trashCans, can, counters):
    rows, cols = trashCans.shape
    trashCans[counters[can], can] += 1
    counters[can] += 1

    if counters[can] == rows:
        return True
    else:
        return False

def displayTrashCans(trashCans):
    rows, cols = trashCans.shape
    for row in reversed(range(rows)):
        row_str = "|".join([str(trashCans[row, col]) for col in range(cols)])
        print(row_str)
        
def main():
    num_trash_cans = getPosInt("Enter the number of trash cans (> 0): ")
    num_bags_per_can = getPosInt("Enter the number of bags per trash can (> 0): ")

    trashCans = np.zeros((num_bags_per_can, num_trash_cans), dtype=int)
    counters = np.zeros(num_trash_cans, dtype=int)

    while True:
        can = getBoundedInt("Enter a trash can number between 0 and %d: " % (num_trash_cans - 1), 0, num_trash_cans - 1)
        if addTrashToCan(trashCans, can, counters):
            print("Trash can %d is full! Time to have the trash picked up." % can)
            break

        displayTrashCans(trashCans)

    print("""
    Programmed by Thanh Dat Nguyen
    Date: %s
    End of processing.""" % ctime())

if __name__ == "__main__":
    main()
