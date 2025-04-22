#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        ans = []
        for i, curr in enumerate(nums):
            if i > 0 and curr == nums[i - 1]:
                continue # 跳过重复的curr
            l, r = i + 1, n - 1
            while l < r:
                s = curr + nums[l] + nums[r]
                if s == 0:
                    ans.append([curr, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
        return ans
        
# @lc code=end

