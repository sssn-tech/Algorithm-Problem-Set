from typing import *
from functools import cmp_to_key

n, m = map(int, input().split())
strs = []

for _ in range(n):
    strs.append(input())


def build_edge(s1: str, s2: str) -> int:
    # 返回两个字符串的最大连续子串长度(环形)
    # 用dp[i][j]表示 s1[?:i]和s2[?:j]的最长连续匹配序列长度
    # dp[i][j] = if == dp[i - 1][j - 1] + 1
    s1_long = s1 + s1
    s2_long = s2 + s2
    dp = [[0 for j in range(2 * m)] for i in range(2 * m)]
    res = 0
    for i in range(2 * m):
        for j in range(2 * m):
            if i == 0 or j == 0:
                if s1_long[i] == s2_long[j]:
                    dp[i][j] = max(dp[i][j], 1)
                    res = max(res, dp[i][j])
            elif s1_long[i] == s2_long[j]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
                res = max(res, dp[i][j])
    return min(res, m)

edges = []
for i in range(n):
    for j in range(n):
        if i != j:
            edges.append((i, j, build_edge(strs[i], strs[j])))

edges.sort(key=cmp_to_key(lambda e1, e2: e2[2] - e1[2])) # 按照边权从大到小排列

parent = [i for i in range(n)]
weight = [1 for _ in range(n)]

def find(u: int) -> int:
    if parent[u] == u:
        return u
    parent[u] = find(parent[u])
    return parent[u]

def union(u: int, v: int) -> None:
    fu, fv = find(u), find(v)
    if fu == fv:
        return 
    # 确保u是大树, v是小树
    if weight[v] > weight[u]:
        u, v = v, u 
    parent[fv] = fu
    weight[fu] += weight[fv]

ans, edge_n = 0, 0
for edge in edges:
    u, v, w = edge 
    fu, fv = find(u), find(v)
    if fu != fv:
        union(u, v)
        ans += w 
        edge_n += 1
    if edge_n == n - 1:
        break
print(ans)

