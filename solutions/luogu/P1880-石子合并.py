from typing import *
from collections import *
from datetime import *
from functools import *
import heapq
import bisect

n = int(input())
n_circle = n * 2
nums = list(map(int, input().split()))
nums = nums + nums # 拼成环形

prefix_sums = []
for num in nums:
    prefix_sums.append(num + (prefix_sums[-1] if prefix_sums else 0))

# 环形石子合并求最大最小代价
# dp[lo][hi]表示合并闭区间[lo, hi]的最小代价
inf = float('inf')
dp_min = [[inf for _ in range(n_circle + 1)] for _ in range(n_circle + 1)]
for i in range(n_circle + 1):
    dp_min[i][i] = 0
dp_max = [[0 for _ in range(n_circle + 1)] for _ in range(n_circle + 1)]


for l in range(2, n + 1): # 区间长度
    for lo in range(n_circle - l + 1): # 区间起点, 环形
        hi = lo + l - 1
        for k in range(lo, hi):
            prefix = prefix_sums[hi] - (prefix_sums[lo - 1] if lo >= 1 else 0)
            dp_min[lo][hi] = min(dp_min[lo][hi], dp_min[lo][k]+dp_min[k+1][hi]+prefix)
            dp_max[lo][hi] = max(dp_max[lo][hi], dp_max[lo][k]+dp_max[k+1][hi]+prefix)

min_res, max_res = inf, 0
for lo in range(0, n):
    hi = lo + n - 1
    min_res = min(min_res, dp_min[lo][hi])
    max_res = max(max_res, dp_max[lo][hi])
print(f'{min_res}\n{max_res}')




