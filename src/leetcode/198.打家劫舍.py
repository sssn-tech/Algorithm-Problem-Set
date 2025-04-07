#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # dp[i]表示截止下标i可以获得的最高收益
        # dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        n = len(nums)      
        dp = [0] * n

        for i in range(n):
            steal = (dp[i - 2] if i >= 2 else 0) + nums[i]
            hold = dp[i - 1]
            dp[i] = max(steal, hold)
        return dp[n - 1]
        
# @lc code=end

