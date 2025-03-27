#
# @lc app=leetcode.cn id=2712 lang=python3
#
# [2712] 使所有字符相等的最小成本
#

# @lc code=start
class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s) - 1
        lo, hi = 0, n 
        ans = 0
        while lo < hi:
            # 这次操作要让[0, lo]->s[lo], [hi, n]->s[hi]
            lo += 1
            hi -= 1
            if lo <= hi:
                if s[lo] != s[lo - 1]:
                    ans += lo
                if s[hi] != s[hi + 1]:
                    ans += lo
            else: # 交错了
                if s[lo] != s[hi]:
                    ans += lo
        return ans

                
                

# @lc code=end

s = Solution()
print(s.minimumCost(input()))
