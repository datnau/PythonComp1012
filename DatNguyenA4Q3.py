#DatNguyenA4Q1.py
#
# Course: COMP 1012
# Instructor: Abolfazl Babaei
# Assignment: 4 Question 2
# Author: Thanh Dat Nguyen
# Version: 2023/12/10
#
# Purpose: 
from time import ctime
import math


def txt2Int(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            numbers.extend(map(int, line.split()))
    return numbers


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return 2
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return True


def PrimeRec(Num):
    prime_set = set()
    non_prime_dict = {}
    
    for number in Num:
        result = is_prime(number)
        if result is True:
            prime_set.add(number)
        else:
            non_prime_dict[number] = [result]
    
    print("Prime set is:")
    print(sorted(prime_set))
    
    print("Dictionary of non-prime numbers and a divisor:")
    print(non_prime_dict)
    print("""
    Programmed by Thanh Dat Nguyen
    Date: %s
    End of processing.""" % ctime())

filename = "A4_Q3.txt"
numbers = txt2Int(filename)
PrimeRec(numbers)