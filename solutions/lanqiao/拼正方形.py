"""
707540323478
7385137888721
"""
from typing import *
from collections import *
from datetime import *
from functools import *
import heapq
import bisect
import math 

n_total_2x2, n_total_1x1 = 7385137888721, 10470245
s_total = n_total_2x2 * 4 + n_total_1x1 

def can_made(a: int) -> bool:
    # 边长为a的正方形能否被拼出来
    if a * a > s_total: 
        return False
    if a % 2 == 0:
        return s_total >= a * a 
    if a * 2 - 1 <= n_total_1x1:
        return s_total >= a * a
    else:
        return False

l, r = 1, int(math.sqrt(s_total)) + 100000000
while l < r:
    mid = (l + r + 1) >> 1
    if not can_made(mid):
        r = mid - 1
    else:
        l = mid

print(f'ans = {l}')