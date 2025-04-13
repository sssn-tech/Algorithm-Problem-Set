from typing import *
from collections import *
from datetime import *
from functools import *
import heapq
import bisect
import math


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        A = list(set(nums))
        if len(A) < 3: return len(A)

        M = 2048
        dp = [0] * 4
        dp[0] = 1  # 初始：使用0个数时只能得到XOR为0

        for x in A:
            for i in range(3, 0, -1):
                m = dp[i - 1]
                while m:
                    b = m & -m
                    v = (b.bit_length() - 1) ^ x
                    dp[i] |= 1 << v
                    m ^= b
            dp[1] |= 1 << x  # 补上 dp[1] 中可能缺少的 x 本身

        return (dp[1] | dp[3]).bit_count()

print(Solution().uniqueXorTriplets([1, 2, 3, 4, 100000000, 4234]))
print(len([0, 1, 2, 3, 4, 5, 6, 7, 4232, 4233, 4234, 4235, 4236, 4237, 4239, 100000000, 100000001, 100000002, 100000003, 100000005, 100000006, 100000007, 100004232, 100004233, 100004235, 100004238]))