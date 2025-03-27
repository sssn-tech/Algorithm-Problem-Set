from typing import *
from collections import *

def edit_distance(s1: str, s2: str) -> int:
    """
    - 用dp[i][j]表示s1[:i]和s2[:j]的最小编辑距离, 注意不包括s1[i]和s2[j]
    - 不对其下标是因为我们需要考虑空子串的情况
    - if s1[i - 1] == s2[j - 1], dp[i][j] = dp[i - 1][j - 1]
    - else dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
    - 要使s1向s2靠拢, 3种对i的操作法, 插入, 删除, 修改
    - 边界条件dp[i][0] = i, dp[0][j] = j, 代表空字符串的编辑距离
    """
    n, m = len(s1), len(s2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = j 
            if j == 0:
                dp[i][j] = i 
            if i > 0 and j > 0:
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)

    return dp[n][m]


_, s1 = input(), input()
_, s2 = input(), input()

print(edit_distance(s1, s2))