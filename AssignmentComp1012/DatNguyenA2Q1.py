#DatNguyenA2Q2.py
#
# Course: COMP 1012
# Instructor: Abolfazl Babaei
# Assignment: 2 Question 1
# Author: Thanh Dat Nguyen
# Version: 2023/10/31
#
# Purpose: 
# var1 - the use / meaning of each variable in the program

from time import ctime
print('\n--------------------------------------------------\n')

def grablist():
    list_size = input("Enter the length of the list: ")
    user_list = []
    for i in range(int(list_size)):
        element = input("Enter element %d: " % (i + 1))
        user_list.append(element)
    return user_list

def listSearch(main_list):
    frequency_dict = {}
    for i, element in enumerate(main_list):
        if element in frequency_dict:
            frequency_dict[element].append(i)
        else:
            frequency_dict[element] = [i]
    return frequency_dict

def delDup(main_list, frequency_dict):
    final_list = []
    for element in main_list:
        if element not in final_list:
            final_list.append(element)
    
    print("The final list is:", final_list)
    for element in frequency_dict:
        print('The element %s occurs %s times at' % (element, len(frequency_dict[element])), end=' ')
        
        for index in frequency_dict[element]:
            print(index, end=',')

        if len(frequency_dict[element]) > 1:
            print("=> It is removed")
        print()

def main():
    main_list = grablist()
    frequency_dict = listSearch(main_list)
    delDup(main_list, frequency_dict)

main()

print("""
Programmed by Thanh Dat Nguyen
Date: %s
End of processing.""" % ctime())


