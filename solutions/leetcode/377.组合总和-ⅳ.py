#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#

from typing import *
from collections import *

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0 for _ in range(target + 1)]
        for num in nums:
            if num <= target:
                dp[num] += 1
        
        for i in range(target + 1):
            for num in nums:
                if num > i:
                    break
                dp[i] += dp[i - num]
        return dp[target]
        
# @lc code=end

s = Solution()
nums = list(map(int, input().split()))
target = int(input())
print(s.combinationSum4(nums, target))