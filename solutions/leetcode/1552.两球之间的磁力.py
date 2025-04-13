#
# @lc app=leetcode.cn id=1552 lang=python3
#
# [1552] 两球之间的磁力
#

# @lc code=start
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def check(mag) -> bool:
            """
            - 能否找到一种摆放, 让所有球的距离不小于mag?
            """
            prev = -10**10
            placed = 0
            for p in position:
                if p - prev >= mag:
                   placed += 1
                   prev = p 
            return placed >= m 
        l, r = 0, 10**10
        while l < r:
            mid = (l + r + 1) >> 1
            if not check(mid):
                r = mid - 1
            else:
                l = mid 
        return l
         


        
# @lc code=end

