# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 20:53:03 2023

@author: ADMIN
"""

fiveNums = []
kNumber = 1
while True:
    if kNumber%2 == 0:
        fiveNums.append(kNumber)
        if len(fiveNums) == 5:
            break
        kNumber += 1