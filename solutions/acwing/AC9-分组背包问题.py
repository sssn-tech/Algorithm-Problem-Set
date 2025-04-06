from typing import *
from collections import *
from datetime import *
from functools import *
import heapq
import bisect

# n组物品, 容量限制v
n, v = map(int, input().split())
dp = [0] * (v + 1) # dp[i]表示容量限制v下的最大收益

for _ in range(n):
    m = int(input())
    items = []
    for __ in range(m):
        c, w = map(int, input().split())
        items.append((c, w))
    for j in range(v, -1, -1):
        for c, w in items:
            dp[j] = max(dp[j], dp[j - c] + w if j >= c else 0)

print(dp[v])
