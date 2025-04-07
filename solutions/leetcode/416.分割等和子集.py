#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)

        if s % 2 == 1:
            return False
        target = s // 2
        stop = False
        @cache
        def dfs(p, s, jumped):
            # 从下标p开始, 找和为s的子集
            nonlocal stop
            if stop:
                return True
            if p >= n:
                return False
            if nums[p] == s:
                stop = True
                return True
            if jumped > target:
                return False        
            sel = dfs(p + 1, s - nums[p], jumped) if s > nums[p] else False
            no_sel = dfs(p + 1, s, jumped + nums[p])
            return sel or no_sel

        return dfs(0, target, 0)
        
# @lc code=end

