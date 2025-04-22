#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda inte: inte[0])
        ans = []
        l_hold, r_hold = intervals[0][0], intervals[0][1]
        for l_curr, r_curr in intervals:
            if l_curr > r_hold:
                ans.append([l_hold, r_hold])
                l_hold, r_hold = l_curr, r_curr
            else:
                r_hold = max(r_hold, r_curr)
        ans.append([l_hold, r_hold])
        return ans
        
# @lc code=end

