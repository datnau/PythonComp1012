#DatNguyenA4Q1.py
#
# Course: COMP 1012
# Instructor: Abolfazl Babaei
# Assignment: 4 Question 2
# Author: Thanh Dat Nguyen
# Version: 2023/12/10
#
# Purpose: 
import random
import numpy as np
from time import ctime

def getValidPositiveNumber(prompt):
    while True:
        try:
            userInput = eval(input(prompt))
            if type(userInput) not in (int, float):
                raise ValueError
            if userInput <= 0:
                raise ValueError
            return userInput
        except ValueError:
            if userInput == "":
                print("Missing input!")
            elif userInput <= 0:
                print("%s is not greater than zero!" % userInput)
            else:
                print("%s is not a number!" % userInput)
        except:
            print("%s is not valid input!" % userInput)

def parabola(h, k, xCoordinates):
    a = -k / h**2
    return a * (xCoordinates - h)**2 + k

def monteCarlo(fx, h, k, points):
    under_parabola = 0
    for _ in range(points):
        x = random.uniform(0, 2*h)
        y = random.uniform(0, k)
        if y <= fx(x):
            under_parabola += 1
    area = (under_parabola / points) * (2*h * k)
    return area

def main():
    noOfPoints = int(getValidPositiveNumber("Enter the number of intervals / points: "))
    h = getValidPositiveNumber("Enter the value of h in cm: ")
    k = getValidPositiveNumber("Enter the value of k in cm: ")
    actual_area = 4 * h * k / 3
    approximate_area = monteCarlo(lambda x: parabola(h, k, x), h, k, noOfPoints)
    error = actual_area - approximate_area
    print("Area computed using the Monte Carlo technique.")
    print("Area is from x=0.00 to x=%s" % (2 * h))
    print("Approximate area of the parabola is %.15e cm^2" % approximate_area)
    print("Actual area of the parabola is %.15e cm^2" % actual_area)
    print("The error in the approximation is %.8e cm^2" % error)
    print("""
    Programmed by Thanh Dat Nguyen
    Date: %s
    End of processing.""" % ctime())
if __name__ == "__main__":
    main()
