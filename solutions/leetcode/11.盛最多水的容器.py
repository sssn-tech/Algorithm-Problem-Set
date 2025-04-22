#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        lo, hi = 0, len(height) - 1
        ans = 0
        while lo < hi:
            ans = max(ans, min(height[lo], height[hi]) * (hi - lo))
            if height[lo] >= height[hi]:
                hi -= 1
            else:
                lo += 1
        return ans
        
# @lc code=end

