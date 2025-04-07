#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        """
        环形的打家劫舍可以分类讨论
        - 如果偷了起始位置
        - 如果不偷起始位置
        """
        n = len(nums)
        ans = nums[0] # 至少可以偷0

        dp = [0] * n 
        # 先算不偷0的, 从1开始到n-1都正常处理
        for i in range(1, n):
            steal = (dp[i - 2] if i >= 2 else 0) + nums[i]
            hold = dp[i - 1]
            dp[i] = max(steal, hold)
        ans = max(ans, dp[n - 1])

        # 再算必须偷0的, 则n-1必须不偷
        dp = [0] * n 
        dp[0] = nums[0]
        for i in range(1, n - 1):
            steal = (dp[i - 2] if i >= 2 else 0) + nums[i]
            hold = dp[i - 1]
            dp[i] = max(steal, hold)
        print(dp)
        ans = max(ans, dp[n - 2] if n >= 2 else 0,
                       dp[n - 3] if n >= 3 else 0)

        return ans

        
# @lc code=end

