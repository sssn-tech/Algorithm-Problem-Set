# 本质上是问有多少个A[i][j]和对角线, 反对角线的元素相等
# 借鉴八皇后的思路: 对角线坐标做差值相等, 反对角线坐标做和相等
# 用两个dict, 一个处理对角线, 一个处理反对角线
# dg[(val, i-j)] = n 代表i-j号对角线上, 值为val的有n个


n, m = map(int, input().split())
nums = []
for i in range(n):
    temp = list(map(int, input().split()))
    nums.append(temp)

from collections import defaultdict
dg, xdg = defaultdict(lambda: 0), defaultdict(lambda: 0)
ans = 0
for i in range(n):
    for j in range(m):
        val = nums[i][j]
        ans += dg.get((val, i - j), 0)
        ans += xdg.get((val, i + j), 0)
        dg[(val, i - j)] += 1
        xdg[(val, i + j)] += 1

print(ans * 2)