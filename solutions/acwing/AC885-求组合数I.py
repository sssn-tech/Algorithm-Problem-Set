
n_max = 2000
mod = int(1e9+7)
c = [[0 for _ in range (n_max + 1)] for _ in range(n_max + 1) ]  

# 递推建表
# c(n, k) = c(n-1, k) + c(n-1, k-1)
for i in range(0, n_max + 1):
    c[i][0] = c[i][i] = 1
    for j in range(1, i):
        c[i][j] = (c[i-1][j] + c[i-1][j-1]) % mod

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    print(c[n][k] % mod)
