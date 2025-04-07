from typing import *
from collections import *
from datetime import *
from functools import *
import heapq
import bisect

# poes = []
# for i in range(1, 500):
#     for j in range(i + 1, 500):
#         # 区间[i, j]求和
#         s = (i + j) * (j - i + 1) // 2
#         if s not in poes:
#             poes.append(s)
# poes.sort()

# print(poes)
# for i in range(500):
#     if i not in poes:
#         print(i)

pow2 = [1]
while pow2[-1] <= 1e16:
    pow2.append(pow2[-1] * 2)
pow2 = set(pow2)
# n & (n - 1) == 0

n = int(input())
nums = list(map(int, input().split()))
ans = 0
for num in nums:
    if  num in pow2:
        ans += 1
print(ans)
