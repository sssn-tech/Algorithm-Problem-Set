#
# @lc app=leetcode.cn id=2266 lang=python3
#
# [2266] 统计打字方案数
#
from typing import *
from functools import *

# @lc code=start
class Solution:
    def strSplit(self, s: str) -> List[str]:
        # 将字符串s切成相同字符的列表
        n = len(s)
        if n == 0 or n == 1:
            return [s]
        res = []
        lo, hi = 0, 1
        while lo <= hi and hi <= n:
            while hi < n and s[hi] == s[hi - 1]:
                hi += 1
            res.append(s[lo:hi])
            lo = hi 
            hi += 1
        return res
    
    @cache
    def combinations(self, l: int, k: int) -> int:
        # 长度为l的楼梯, 每次可以走1-k阶, 返回方案数
        mod = int(1e9 + 7)
        dp = [0 for _ in range(l + 1)]
        for i in range(1, k + 1):
            if i <= l:
                dp[i] += 1
            else:
                break
        for i in range(1, l + 1):
            for j in range(1, k + 1):
                if i - j >= 0:
                    dp[i] += dp[i - j]
                    dp[i] %= mod
                else:
                    break
            dp[i] %= mod
        return dp[l] % mod

    def countTexts(self, pressedKeys: str) -> int:
        # 首先要把字符串切开分析, 比如22233要切成222和33
        # 然后dp分析, 这么多数字其实只有两类, 3key的和4key的
        ss = self.strSplit(pressedKeys)
        ans = 1
        mod = int(1e9 + 7)
        for s in ss:
            ans *= self.combinations(len(s), 4 if int(s[0]) == 7 or int(s[0]) == 9 else 3)
            ans %= mod
        return ans
# @lc code=end


s = input()
print(Solution().countTexts(s))