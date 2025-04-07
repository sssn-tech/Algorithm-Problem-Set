# 2024041331404202

from typing import *
from collections import *
from datetime import *
from functools import *
import heapq
import bisect


# A(i) = (1 + i) / 2 * i
# B(i) = 1 * 2 * 3 * ... * i
s = 0
m = 1
for i in range(1, 1000):
    s += i 
    m *= i 
    if (s - m) % 100 == 0:
        print(i)
END = 2024041331404202
print(END // 200, END % 200)
print(END // 200 * 4 + 2)

