#
# @lc app=leetcode.cn id=2563 lang=python3
#
# [2563] 统计公平数对的数目
#

# @lc code=start
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)

        ans = 0
        for i, num in enumerate(nums):
            le = max(i + 1, bisect.bisect_left(nums, lower - num, i, n))
            ri = max(i + 1, bisect.bisect_right(nums, upper - num, i, n))
            ans += max(ri - le, 0)
        return ans


        
# @lc code=end

