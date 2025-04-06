from typing import *
from collections import *
from datetime import *
from functools import *
import heapq
import bisect

n = int(input())
n_circle = n * 2
nums = list(map(int, input().split()))
nums = nums + nums # 成环

dp = [[0 for _ in range(n_circle + 1)] for _ in range(n_circle + 1)]


for l in range(3, n + 2): # 区间长度
    for lo in range(0, n_circle - l + 1): # 区间起点
        hi = lo + l - 1
        for k in range(lo + 1, hi):
            val = dp[lo][k]+dp[k][hi]+nums[lo]*nums[k]*nums[hi]
            dp[lo][hi] = max(dp[lo][hi], val)

ans = max(dp[lo][lo+n] for lo in range(n))
print(ans)
# for line in dp:
#     print(line)



