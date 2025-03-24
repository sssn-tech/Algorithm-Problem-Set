from typing import *

def max_gain_double(field: List[List[int]], n: int) -> int:
    # 返回n x n的棋盘格field中, 从左上角走到右下角, 走两次, 单独取数的最大收益
    # dp[i1][j1][i2][j2] 表示第一次走到i1, j2, 第二次走到i2, j2的最大收益
    # 要到达这个状态, 有4种转移方法, 分别是一右二右, 一右二下, 一下二右, 一下二下
    # dp[i1][j1][i2][j2] = max(dp[i1][j1-1][i2][j2-1], dp[i1][j1-1][i2-1][j2], dp[i1-1][j1][i2][j2-1], dp[i1-1][j1][i2-1][j2])
    dp = [[[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
    dp[0][0][0][0] = field[0][0] * 2 # 循环里面减掉
    for i1 in range(n):
        for j1 in range(n):
            for i2 in range(n):
                for j2 in range(n):
                    if i1 > 0 and i2 > 0:
                        dp[i1][j1][i2][j2] = max(dp[i1][j1][i2][j2], dp[i1-1][j1][i2-1][j2] + field[i1][j1] + field[i2][j2])
                    if i1 > 0 and j2 > 0:
                        dp[i1][j1][i2][j2] = max(dp[i1][j1][i2][j2], dp[i1-1][j1][i2][j2-1] + field[i1][j1] + field[i2][j2])
                    if j1 > 0 and i2 > 0:
                        dp[i1][j1][i2][j2] = max(dp[i1][j1][i2][j2], dp[i1][j1-1][i2-1][j2] + field[i1][j1] + field[i2][j2])
                    if j1 > 0 and j2 > 0:
                        dp[i1][j1][i2][j2] = max(dp[i1][j1][i2][j2], dp[i1][j1-1][i2][j2-1] + field[i1][j1] + field[i2][j2])
                    if i1 == i2 and j1 == j2: # 一个位置只能拿一次
                        dp[i1][j1][i2][j2] -= field[i1][j1]
    return dp[n - 1][n - 1][n - 1][n - 1]




n = int(input()) # 这道题的n是1-based, 编码时候转为0-based
field = [[0 for j in range(n)] for i in range(n)]

x, y, z = map(int, input().split())
while not (x == 0 and y == 0 and z == 0):
    field[x - 1][y - 1] = z 
    x, y, z = map(int, input().split())

print(max_gain_double(field, n))

