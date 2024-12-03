# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 19:14:21 2024

@author: kefke
"""
import numpy as np
import math
from collections import Counter
import re

info = open("Day3.txt", "r").read()

### part 1
values = [int(x)*int(y) for x,y in re.findall(r'mul\((\d+),(\d+)\)', info)]

print('The answer to part 1 is:', sum(values))

### part 2
active = True
ans2 = 0
new_info = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", info)
for x,y, do, dont in new_info:
    if active and x != '' and y !='':
        ans2 += int(x)*int(y)
    if do:
        active = True
    elif dont:
        active = False
        
print('The answer to part 2 is:', ans2)