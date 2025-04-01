#
# @lc app=leetcode.cn id=2140 lang=python3
#
# [2140] 解决智力问题
#
from typing import *
from collections import *
from datetime import *
from functools import *
import heapq
import bisect

# @lc code=start
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        @cache
        def dfs(p: int) -> int:
            if p >= n:
                return 0
            # 做或者不做
            val, cost = questions[p]
            return max(dfs(p+1), dfs(p+cost+1) + val)
        return dfs(0)

        
# @lc code=end

