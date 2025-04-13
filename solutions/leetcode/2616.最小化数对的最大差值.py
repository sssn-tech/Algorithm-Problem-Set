#
# @lc app=leetcode.cn id=2616 lang=python3
#
# [2616] 最小化数对的最大差值
#

# @lc code=start
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def check(nums, p, k) -> bool:
            """
            - nums中能否找到p对数字, 他们的最大差值不大于k
            """
            i, cnt = 0, 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= k:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= p

        l, r = 0, 10**9
        while l < r:
            mid = (l + r) >> 1
            if not check(nums, p, mid):
                l = mid + 1
            else:
                r = mid

        return l


        
# @lc code=end

