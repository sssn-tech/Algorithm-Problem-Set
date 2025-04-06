from typing import *
from collections import *
from datetime import *
from functools import *
import heapq
import bisect

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_ok(nums):
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    return False
            return True
        
        ans = 0
        while not is_ok(nums):
            ans += 1
            p, q, s = 0, 0, 1000000000000
            for i in range(1, len(nums)):
                if nums[i] + nums[i - 1] < s:
                    p, q = i - 1, i
                    s = nums[i] + nums[i - 1]
            nums[p] = nums[p] + nums[q]
            del nums[q]
        return ans
    
print(Solution().minimumPairRemoval([5, 2, 3, 1]))
