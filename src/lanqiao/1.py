
from typing import *
from collections import *
from datetime import *
from functools import *
import heapq
import bisect

from typing import List, Tuple
import math

def bin_lifting_lca(adj_list: List[List[int]], root: int, queries: List[Tuple[int, int]]) -> List[int]:
    n = len(adj_list)
    LOG = math.ceil(math.log2(n)) + 1  # 最大倍增层数

    parent = [[-1] * LOG for _ in range(n)]  # parent[node][k] 表示 node 的 2^k 级祖先
    depth = [0] * n
    visited = [False] * n

    def dfs(u: int, p: int):
        visited[u] = True
        parent[u][0] = p
        for v in adj_list[u]:
            if not visited[v]:
                depth[v] = depth[u] + 1
                dfs(v, u)

    # Step 1: DFS 初始化 parent[0] 和 depth
    dfs(root, -1)

    # Step 2: 预处理所有 2^k 级祖先
    for k in range(1, LOG):
        for v in range(n):
            if parent[v][k - 1] != -1:
                parent[v][k] = parent[parent[v][k - 1]][k - 1]

    def get_lca(u: int, v: int) -> int:
        if depth[u] < depth[v]:
            u, v = v, u

        # Step 3: 将 u 提升到和 v 同一深度
        for k in reversed(range(LOG)):
            if parent[u][k] != -1 and depth[parent[u][k]] >= depth[v]:
                u = parent[u][k]

        if u == v:
            return u

        # Step 4: 同时向上跳，直到找到 LCA
        for k in reversed(range(LOG)):
            if parent[u][k] != -1 and parent[u][k] != parent[v][k]:
                u = parent[u][k]
                v = parent[v][k]

        return parent[u][0]

    # Step 5: 处理所有查询
    return [get_lca(u, v) for u, v in queries]

n, m, s = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

queries = []
for _ in range(m):
    u, v = map(int, input().split())
    queries.append((u, v))

ans = bin_lifting_lca(graph, s, queries)
for u in ans:
    print(u)
    

