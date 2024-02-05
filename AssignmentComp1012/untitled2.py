import timeit
from math import sqrt
from time import ctime

def getNonNegativeInt(prompt):
    while True:
        number = input(prompt).strip()
        if number != '':
            try:
                number = int(number)
            except ValueError:
                print('Invalid input!')
            else:
                if number >= 0:
                    break
                else:
                    print(number, 'must not be negative!')
        else:
            print('Missing input!')
            
    return number

def computeXcoordinates(width, intervals):
    x = width / intervals
    xCoords = [-width/2 + i*x for i in range(intervals)]
    return xCoords

def computeYcoordinates(xCoords):
    y1Coords = [sqrt(1-(abs(x)-1)**2) for x in xCoords]
    y2Coords = [-3*sqrt(1-sqrt(abs(x)/2)) for x in xCoords]
    return y1Coords, y2Coords

def computeArea(intervals, width):
    xCoords = computeXcoordinates(width, intervals)  # Fix function name here
    y1Coords, y2Coords = computeYcoordinates(xCoords)  # Fix function name here
    h = width / (intervals - 1)
    upperArea = (h / 2) * (y1Coords[0] + 2 * sum(y1Coords[1:intervals - 1]) + y1Coords[intervals - 1])
    lowerArea = (h / 2) * (y2Coords[0] + 2 * sum(y2Coords[1:intervals - 1]) + y2Coords[intervals - 1])
    area = upperArea - lowerArea
    print(f"Area of heart is: {area} cm square")

def displayTerminationMessage():
    print("""
    Programmed by Thanh Dat Nguyen
    Date: %s
    End of processing.""" % ctime())

width = 4
intervals = getNonNegativeInt("Enter the number of intervals (0 to quit): ")
while intervals != 0:
    t = timeit.Timer('computeArea(intervals, width)', 'from __main__ import computeArea, intervals, width')
    computeTime = t.timeit(1)
    print("Compute time using lists is %.3f seconds."%computeTime)
    intervals = getNonNegativeInt("Enter the number of intervals (0 to quit): ")

displayTerminationMessage()
