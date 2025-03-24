# 用dp[i][j=0,1][k=0,2,4]表示要到达下标i的位置, 最后一次操作者是j, 最后一次操作使用咒语k, 能进行的最多迁移次数

from typing import *

n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

dp = [[[0 for k in range(5)] for j in range(2)] for i in range(n)]

def decom(num: int) -> List[int]:
    res = []
    num_str = str(num)
    if '0' in num_str:
        res.append(0)
    if '2' in num_str:
        res.append(2)
    if '4' in num_str:
        res.append(4)
    return res

for i in range(n):
    num0, num1 = s[i], t[i]
    set0, set1 = decom(num0), decom(num1)
    dp[i][0][0] = (1 if 0 in set0 else 0)
    dp[i][0][2] = (1 if 2 in set0 else 0)
    dp[i][0][4] = (1 if 4 in set0 else 0)
    if i > 0: 
        dp[i] = dp[i - 1] # 先转移上一个状态
        for num in set0:
            dp[i][0][num] = max(dp[i][0][num], 1) # 任意位置0号都可以直接启动
        for num in set0:
            if dp[i - 1][1][num] != 0:
                dp[i][0][num] = max(dp[i][0][num], dp[i - 1][1][num] + 1)
        for num in set1:
            if dp[i - 1][0][num] != 0:
                dp[i][0][num] = max(dp[i][0][num], dp[i - 1][1][num] + 1)