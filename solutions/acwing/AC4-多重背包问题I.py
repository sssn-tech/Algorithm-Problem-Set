from typing import *
from collections import *
from datetime import *
from functools import *
import heapq
import bisect

# n个物品, 空间限制v
n, v = map(int, input().split())
items = []

def build_items(c, w, m) -> None:
    # 将m个代价为c, 收益为w分解为2进制个数的物品
    k = 1
    while m >= k:
        items.append((c * k, w * k))
        m -= k
        k <<= 1
    if m > 0:
        items.append((c * m, w * m))

for _ in range(n):
    # 代价, 收益, 个数
    c, w, m = map(int, input().split())
    build_items(c, w, m)

# 这里开始就是朴素的0-1背包了
n = len(items)
dp = [0] * (v + 1)
for c, w in items:
    for j in range(v, c - 1, -1):
        dp[j] = max(dp[j], dp[j - c] + w)

print(dp[v])
