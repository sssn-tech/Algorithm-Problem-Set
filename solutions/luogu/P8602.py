# 如果要走L距离, 花费将是Cost = (1 + 10) + (2 + 10) + (3 + 10) + ... + (L + 10)
# Cost = (21 + L) / 2 * L

from typing import *

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def treeD(graph: List[List[Tuple[int, int]]], n: int, root: int) -> int:
    # 求一棵树的直径
    def dfs(u: int) -> Tuple[int, int]:
        # 求树上一个点能到达的最远点和距离
        nonlocal n
        vis = [False for _ in range(n + 1)]
        far, cost_max = 0, -1
        stack = [(u, 0)] # 模拟递归栈
        while len(stack) != 0:
            curr, cost = stack.pop()
            vis[curr] = True
            if cost > cost_max:
                cost_max = cost
                far = curr
            for v, w in graph[curr]:
                if not vis[v]:
                    stack.append((v, cost + w))
        return far, cost_max
    
    far, _ = dfs(root)
    _, d = dfs(far)
    return d
        

d = treeD(graph, n, 1)
print((21 + d) * d // 2)