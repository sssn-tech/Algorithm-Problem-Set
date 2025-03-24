from typing import *

def pass_note(field: List[List[int]], n: int, m: int) -> int:
    # 在n行m列的field之中传纸条
    # 等价为左上角到右下角走两次, 路径不可交汇(每个同学只帮一次忙)
    # i1j1走下方路径, i2j2走上方路径
    dp = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
    for i1 in range(n):
        for j1 in range(m):
            for i2 in range(i1 + 1, n):
                for j2 in range(j1):
                    res = field[i1][j1] + field[i2][j2]
                    if i1 > 0 and i2 > 0:
                        res = max(res, dp[i1-1][j1][i2-1][j2] + field[i1][j1] + field[i2][j2])
                    if i1 > 0 and j2 > 0:
                        res = max(res, dp[i1-1][j1][i2][j2-1] + field[i1][j1] + field[i2][j2])
                    if j1 > 0 and i2 > 0:
                        res = max(res, dp[i1][j1-1][i2-1][j2] + field[i1][j1] + field[i2][j2])
                    if j1 > 0 and j2 > 0:
                        res = max(res, dp[i1][j1-1][i2][j2-1] + field[i1][j1] + field[i2][j2])
                    dp[i1][j1][i2][j2] = res
    # 右下角是不可达的, 返回这个点的左侧和上侧即可
    return dp[n-2][m-1][n-1][m-2]

n, m = map(int, input().split())
field = []
for _ in range(n):
    row = list(map(int, input().split()))
    field.append(row)

print(pass_note(field, n, m))

