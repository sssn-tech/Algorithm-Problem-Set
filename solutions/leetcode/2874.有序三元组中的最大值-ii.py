#
# @lc app=leetcode.cn id=2874 lang=python3
#
# [2874] 有序三元组中的最大值 II
#

# @lc code=start
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_max = [0 for _ in range(n)]
        suffix_max = [0 for _ in range(n)]
        for i in range(n):
            prefix_max[i] = nums[i]
            suffix_max[-i - 1] = nums[-i - 1]
            if i > 0:
                prefix_max[i] = max(prefix_max[i], prefix_max[i - 1])
                suffix_max[-i - 1] = max(suffix_max[-i - 1], suffix_max[-i])
        
        ans = 0
        for j in range(1, n - 1):
            ans = max(ans, (prefix_max[j - 1] - nums[j]) * suffix_max[j + 1])
            
        return ans
        
# @lc code=end

