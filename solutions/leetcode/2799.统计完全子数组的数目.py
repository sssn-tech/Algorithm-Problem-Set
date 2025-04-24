#
# @lc app=leetcode.cn id=2799 lang=python3
#
# [2799] 统计完全子数组的数目
#

# @lc code=start
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(set(nums))
        counter = defaultdict(int)

        lo, hi, ans = 0, 0, 0
        while hi < len(nums):
            counter[nums[hi]] += 1
            while len(counter) == n:
                ans += len(nums) - hi 
                counter[nums[lo]] -= 1
                if counter[nums[lo]] == 0:
                    del counter[nums[lo]]
                lo += 1
            hi += 1
        return ans


        
# @lc code=end

