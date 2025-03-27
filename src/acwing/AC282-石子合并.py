from typing import *
from collections import *

def stone_merge(stones: List[int]) -> int:
    # 用dp[i][j]表示合并闭区间[i, j]所需的最小代价
    n = len(stones)
    inf = int(1e9 + 10)
    prefix_sum = []
    for stone in stones:
        prefix = 0 if not prefix_sum else prefix_sum[-1]
        prefix_sum.append(prefix + stone)
    
    dp = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0 # 合并长度为1的区间不需要代价

    for l in range(2, n + 1): # 区间长度
        for lo in range(n - l + 1): # 区间起点
            hi = lo + l - 1
            # 合并这个区间的开销=历史开销+区间重量(前缀和)
            for k in range(lo, hi):
                prefix = prefix_sum[hi] - (0 if lo ==0 else prefix_sum[lo - 1])
                dp[lo][hi] = min(dp[lo][hi], dp[lo][k] + dp[k+1][hi] + prefix)

    return dp[0][n - 1]

n = int(input())
nums = list(map(int, input().split()))

print(stone_merge(nums))

