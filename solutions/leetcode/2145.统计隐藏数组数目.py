#
# @lc app=leetcode.cn id=2145 lang=python3
#
# [2145] 统计隐藏数组数目
#

# @lc code=start
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        
        curr, min_in_nums, max_in_nums = 0, 0, 0
        for diff in differences:
            curr += diff 
            min_in_nums = min(min_in_nums, curr)
            max_in_nums = max(max_in_nums, curr)
        
        return max(0, upper - lower - max_in_nums + min_in_nums + 1)
        
# @lc code=end

