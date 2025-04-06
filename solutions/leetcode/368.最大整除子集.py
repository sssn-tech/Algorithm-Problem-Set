#
# @lc app=leetcode.cn id=368 lang=python3
#
# [368] 最大整除子集
#

# @lc code=start


"""
把nums排序一下, 就变成了求最长整除子序列
子序列的每一个元素, 都是前面元素的整数倍
用dp[i]表示以下标i结尾的最长整除子序列长度
dp[i] = max({dp[j] if nums[i] % nums[j] == 0} + 1)
"""
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2:
            return nums 
        nums.sort()

        dp = [0] * n # dp[i]表示以nums[i]结尾的最长整除子序列长度
        prev = [-1] * n # prev[i]表示以nums[i]结尾的最长合法子序列的前一个元素位置
        ans_end = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
                    if dp[i] > dp[ans_end]:
                        ans_end = i 
        ans = []
        while ans_end != -1:
            ans.append(nums[ans_end])
            ans_end = prev[ans_end]
        ans.reverse()
        
        return ans



        

        
        
# @lc code=end

