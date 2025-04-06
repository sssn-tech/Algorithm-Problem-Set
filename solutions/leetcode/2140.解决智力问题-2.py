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
        if n == 0:
            return 0
        if n == 1:
            return questions[0][0]
        
        dp = [0 for _ in range(n)]
        dp[n-1] = questions[n-1][0]
        # dp[i]表示从下标i开始到结尾的最大收益
        for i in range(n - 2, -1, -1):
            dp[i] = max(dp[i+1], 
                        questions[i][0] + (0 if i + questions[i][1] + 1 >= n 
                                             else dp[i + questions[i][1] + 1]))
        return dp[0]

        
# @lc code=end

