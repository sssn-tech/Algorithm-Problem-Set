from typing import *
from collections import *
from datetime import *
from functools import *
import heapq
import bisect

n, m = map(int, input().split())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

    # 预计算2的幂次，pow2[i]对应2^i
    pow2 = [1]  # pow2[0] = 1，方便后续计算
    for i in range(1, 100 + 1):
        pow2.append(pow2[-1] * 2)



def max_score(nums):
    n = len(nums)
    if n == 0:
        return 0
    
    mem: Dict[Tuple[int, int], int] = {}
    def dfs(lo: int, hi: int) -> int:
        # nums的闭区间子数组[lo, hi]能获得的最大收益
        if (lo, hi) in mem:
            return mem[(lo, hi)]
        curr_pow = pow2[n - (hi - lo)]
        if lo == hi:
            mem[(lo, hi)] = nums[lo] * curr_pow
            return mem[(lo, hi)]
        res = max(dfs(lo+1, hi)+nums[lo]*curr_pow, 
                  dfs(lo, hi-1)+nums[hi]*curr_pow)
        mem[(lo, hi)] = res
        return res
        
    return dfs(0, n - 1)

ans = 0
for row in matrix:
    ans += max_score(row)
print(ans)