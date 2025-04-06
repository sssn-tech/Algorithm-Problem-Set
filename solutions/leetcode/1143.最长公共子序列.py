#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        # 用dp[i][j]表示text1[:i], text2[:j]的最长公共子序列长度

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]

# @lc code=end



s = Solution()
s1, s2 = input().split()
print(s.longestCommonSubsequence(s1, s2))