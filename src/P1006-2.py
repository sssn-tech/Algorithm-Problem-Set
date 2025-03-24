from typing import *

n, m = map(int, input().split())
field = []
for _ in range(n):
    row = list(map(int, input().split()))
    field.append(row)

dp = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
# x1, y1是下面的线, x2, y2是上面的线
for x1 in range(n):
    for y1 in range(m):
        for x2 in range(x1):
            for y2 in range(y1+1, m):
                sum = field[x1][y1] + field[x2][y2]
                res = sum 
                if x1 > 0 and x2 > 0:
                    res = max(res, dp[x1-1][y1][x2-1][y2]+sum)
                if x1 > 0 and y2 > 0:
                    res = max(res, dp[x1-1][y1][x2][y2-1]+sum)
                if y1 > 0 and x2 > 0:
                    res = max(res, dp[x1][y1-1][x2-1][y2]+sum)
                if y1 > 0 and y2 > 0:
                    res = max(res, dp[x1][y1-1][x2][y2-1]+sum)
                dp[x1][y1][x2][y2] = res
                

print(dp[n-1][m-2][n-2][m-1])