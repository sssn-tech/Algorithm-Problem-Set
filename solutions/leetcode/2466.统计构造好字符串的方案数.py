#
# @lc app=leetcode.cn id=2466 lang=python3
#
# [2466] 统计构造好字符串的方案数
#

# @lc code=start
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = int(1e9 + 7)
        dp = [0] * (high + 1)
        dp[zero] += 1
        dp[one] += 1
        ans = 0
        for i in range(high + 1):
            if i >= zero:
                dp[i] += dp[i - zero]
            if i >= one:
                dp[i] += dp[i - one]
            dp[i] %= mod 
            if i >= low and i <= high:
                ans += dp[i]
                ans %= mod
        return ans
        
# @lc code=end

