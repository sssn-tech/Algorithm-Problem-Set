from typing import *
from collections import *
from datetime import *
from functools import *
import heapq
import bisect

# n件物品, 容量为v
n, v = map(int, input().split())
cs, ws = [-1], [-1] # 填充0来实现1-based下标
for _ in range(n):
    c, w = map(int, input().split())
    cs.append(c)
    ws.append(w)

dp = [0 for _ in range(v + 1)]

for i in range(1, n + 1): # 枚举物品下标1-n
    lo1 = cs[i] - 1 # cs是代价, ws是收益
    lo2 = v - sum(cs[i:])
    for j in range(v, max(lo1, lo2), -1):       
        dp[j] = max(dp[j], dp[j - cs[i]] + ws[i])

print(dp[v])

