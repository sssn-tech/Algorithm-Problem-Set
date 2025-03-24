

bx, by, hx, hy = map(int, input().split())

dp = [[0 for _ in range(by + 1)] for _ in range(bx + 1)]
dp[0][0] = 1

dxs = [1, 1, -1, -1, 2, 2, -2, -2]
dys = [2, -2, 2, -2, 1, -1, 1, -1]

banned = [(hx + dx, hy + dy) for dx, dy in zip(dxs, dys)]
banned.append((hx, hy))

for i in range(bx + 1):
    for j in range(by + 1):
        if (i, j) in banned:
            continue
        if i > 0:
            dp[i][j] += dp[i - 1][j]
        if j > 0:
            dp[i][j] += dp[i][j - 1]
print(dp[bx][by])
# print(dp)
