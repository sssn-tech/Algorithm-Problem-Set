#
# @lc app=leetcode.cn id=2560 lang=python3
#
# [2560] 打家劫舍 IV
#

# @lc code=start
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def can_do(hi, kpi) -> bool:
            # 最大偷hi, 最少偷kpi个, 不能连续偷, 能不能偷
            # dp[i]表示截止下标i最多能偷几个
            dp = [0] * n 
            for i in range(n):
                steal = 1 if nums[i] <= hi else 0 # i能不能偷
                steal += dp[i - 2] if i >= 2 else 0 # 转移之前的偷法
                hold = dp[i - 1]
                dp[i] = max(steal, hold)
            return dp[n - 1] >= kpi

        l, r = min(nums), max(nums)
        while l < r:
            mid = (l + r) >> 1
            if not can_do(mid, k): # hi太低了
                l = mid + 1
            else:
                r = mid
        return l 
        
        
# @lc code=end

print(Solution().minCapability([2,3,5,9], 2))