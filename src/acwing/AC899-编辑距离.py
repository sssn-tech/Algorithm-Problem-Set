from typing import *
from collections import *
"""
[[0, 1, 2, 0], 
[1, 0, 1, 0], 
[0, 0, 0, 0]]
"""
def edit_distance_with_constrain(s1: str, s2: str, k: int) -> bool:
    n, m = len(s1), len(s2)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                dp[i][j] = j 
            if j == 0:
                dp[i][j] = i 
            if i > 0 and j > 0:
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    # print(dp)
    return dp[n][m] <= k

n, m = map(int, input().split())
ss = []
for _ in range(n):
    ss.append(input())

for _ in range(m):
    s1, k = input().split()
    k = int(k)
    res = 0
    for s2 in ss:
        if edit_distance_with_constrain(s1, s2, k):
            res += 1
    print(res)




