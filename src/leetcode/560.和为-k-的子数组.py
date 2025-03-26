#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start

# type: ignore
# 要枚举有多少组i, j满足sum[j] - sum[i-1] = k
# 可以枚举j, 对每个j, 问有多少i满足sum[j]-k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_counter = defaultdict(int)
        prefix_sum_counter[0] += 1
        prefix_sum_curr = 0
        ans = 0

        for j, num in enumerate(nums):
            prefix_sum_curr += num
            ans += prefix_sum_counter[prefix_sum_curr-k]
            prefix_sum_counter[prefix_sum_curr] += 1
            # print(j, ans, prefix_sum_curr, prefix_sum_counter)
        return ans


# @lc code=end

