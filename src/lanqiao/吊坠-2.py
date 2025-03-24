from typing import *
import heapq


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

graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            w = build_edge(strs[i], strs[j])
            graph[i].append((j, w))
            graph[j].append((i, w))

def primMST(graph: List[List[Tuple[int, int]]]) -> int:
    # 0-based primMST
    # 注意本题求最大生成树
    inf = int(1e8 + 10)
    dist = [-inf for _ in range(n)] # 每个点距离MST的距离
    MSTnodes = set()
    MSTlen = 0
    pq = []

    # 以0为起点
    dist[0] = 0
    heapq.heappush(pq, (-0, 0))

    while pq:
        d, u = heapq.heappop(pq)
        d = -d # 还原负数
        if u in MSTnodes:
            continue
        MSTnodes.add(u)
        MSTlen += d 

        for v, w in graph[u]:
            if v not in MSTnodes and dist[v] < w:
                dist[v] = w
                heapq.heappush(pq, (-w, v))
    return MSTlen if len(MSTnodes) == n else inf

print(primMST(graph))