# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:03:03 2024

@author: kevin
"""
import numpy as np
import math
from collections import Counter

info = open("Day1.txt", "r").read().split('\n')
lst_left = []
lst_right = []
for lines in info:
    l, r = lines.split('   ')
    lst_left.append(l)
    lst_right.append(r)

lst_left.sort()
lst_right.sort()

dst = []
lst_sim = []

count = Counter(lst_right)

for i in range(len(lst_left)):
    left = int(lst_left[i])
    right = int(lst_right[i])
    distance = np.abs(left-right)
    dst.append(distance)
    lst_sim.append(count[lst_left[i]]*left)
    
print('The answer to part 1 is:',sum(dst))
print('The answer to part 2 is:',sum(lst_sim))