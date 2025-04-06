#
# @lc app=leetcode.cn id=2829 lang=python3
#
# [2829] k-avoiding 数组的最小总和
#

# @lc code=start
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        ans, curr = 0, 1
        s = set()
        while n > 0:
            if k - curr not in s:
                n -= 1
                s.add(curr)
                ans += curr
            curr += 1
        return ans
        
# @lc code=end

