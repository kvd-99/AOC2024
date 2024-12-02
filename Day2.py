# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:43:27 2024

@author: kefke
"""

import numpy as np
import math
from collections import Counter

info = open("Day2.txt", "r").read().split('\n')
count = 0

### Part 1
# for lines in info:
#     line = lines.split(' ')
#     line = [int(number) for number in line]
#     if all(i < j+3 for i,j in zip((line), line[1:])) or all(j < i for i,j in zip((line), line[1:])):
#         diff = [line[i+1]-line[i] for i in range(len(line)-1)]
#         if all([1<=el<=3 for el in diff]) or all(-3<=el<=-1 for el in diff):
#             count += 1
            
### Part 2
count2 = 0

def safe(line):
    diff = [line[i+1]-line[i] for i in range(len(line)-1)]
    return all([1<=el<=3 for el in diff]) or all(-3<=el<=-1 for el in diff)

for lines in info:
    line = lines.split(' ')
    line = [int(number) for number in line]
    if safe(line):
        count += 1
    elif any(safe(line[:i] + line[i+1:]) for i in range(len(line))):
        count2 += 1
        
print('The answer to part 1 is:', count)
print('The answer to part 2 is:', count + count2)
