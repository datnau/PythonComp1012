#DatNguyenA3Q1.py
#
# Course: COMP 1012
# Instructor: Abolfazl Babaei
# Assignment: 3 Question 1
# Author: Thanh Dat Nguyen
# Version: 2023/11/19
#
# Purpose: Compute the approximate area of a heart using lists and time the computation.
# var1 - the use / meaning of each variable in the program

import timeit
from math import sqrt
from time import ctime
print('\n--------------------------------------------------\n')
def getNonNegativeInt(prompt):
    while True:
        number = input(prompt).strip()
        if number != '':
            try:
                number = eval(number, {}, {})
            except:
                print(number, 'Invalid input')
            else:
                if type(number) is int:
                    if number >= 0:
                        break
                    else:
                        print(number, 'must not be negative!')
                else:
                    print(number, 'must be an integer')
        else:
            print("Missing input!")
    return number


def computeXcoordinates(width, intervals):
    x = [(-width/2) + i * width/(intervals-1) for i in range(intervals)]
    return x

def computeYcoordinates(xCoords):
    y1Coords = [sqrt(1 - (abs(x) - 1)**2) for x in xCoords]
    y2Coords = [-3 * sqrt(abs(1 - sqrt(abs(x) / 2))) for x in xCoords]
    return y1Coords, y2Coords

def computeArea(intervals, width):
    xCoord = computeXcoordinates(width, intervals)
    y1Coord, y2Coord = computeYcoordinates(xCoord)
    h = width / (intervals - 1)
    upperArea = (h / 2) * (y1Coord[0] + 2 * sum(y1Coord[1:intervals - 1]) + y1Coord[intervals - 1])
    lowerArea = (h / 2) * (y2Coord[0] + 2 * sum(y2Coord[1:intervals - 1]) + y2Coord[intervals - 1])
    area = upperArea - lowerArea
    print("The approximate area of the heart is %.14e cm^2"%area)

def displayTerminationMessage():
    print("""
    Programmed by Thanh Dat Nguyen
    Date: %s
    End of processing.""" % ctime())

width = 4
intervals = 0

width = 4
intervals = getNonNegativeInt("Enter the number of intervals (0 to quit): ")
while intervals != 0:
    t = timeit.Timer('computeArea(intervals, width)', 'from __main__ import computeArea, intervals, width')
    computeTime = t.timeit(1)
    print("Compute time using lists is %.3f seconds." % computeTime)
    intervals = getNonNegativeInt("Enter the number of intervals (0 to quit): ")

displayTerminationMessage()
