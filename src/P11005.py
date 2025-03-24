# 一张无向带权图, 定义一条路径的cost为路径包含边权的最大值
# 求图中两点间存在合法路径点点对计数和, 合法指[l, r]

from typing import *

n, m, l, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    if w <= r:
        graph[u].append(v)
        graph[v].append(u)

def graph_count_node(graph: List[List[int]]) -> int:
    vis = [False] * len(graph)
    res = 0
    def dfs(curr: int) -> None:
        vis[curr] = True
        nonlocal res
        res += 1
        for v in graph[curr]:
            if not vis[v]:
                dfs(v)
    dfs(1)
    return res 

n_node = graph_count_node(graph)
ans = (1 + (n_node - 1)) // 2 * n_node
print(ans)