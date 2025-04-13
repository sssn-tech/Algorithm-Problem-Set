#
# @lc app=leetcode.cn id=2439 lang=python3
#
# [2439] 最小化数组中的最大值
#

# @lc code=start
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def can_do(nums, k) -> bool:
            # 能否将nums操作到最大值为k
            # 贪心操作从右到左
            extra = 0
            for i in range(len(nums) - 1, 0, -1):
                if nums[i] > k:
                    extra += nums[i] - k
                else:
                    extra -= k - nums[i]
                    extra = max(extra, 0)

            return nums[0] + extra <= k
        
        l, r = min(nums), max(nums)
        while l < r:
            mid = (l + r) >> 1
            if not can_do(nums, mid):
                l = mid + 1
            else:
                r = mid 
        return l
        
# @lc code=end

