from typing import *
from collections import *
from datetime import *
from functools import *
import heapq
import bisect


n, v = map(int, input().split())
items = []
for _ in range(n):
    c, w = map(int, input().split())
    items.append((c, w))

dp = [0] * (v + 1)

for j in range(1, v + 1):
    for c, w in items:
        if j >= c:
            dp[j] = max(dp[j], dp[j - c] + w)
print(dp[v])